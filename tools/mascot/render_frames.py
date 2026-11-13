#!/usr/bin/env python3
"""Render the MascotWave loop from body.png + hand.png (Pillow only).

The timing mirrors prototype/mascot-wave/mascot-wave.css exactly: the same
keyframes, the same `ease-in-out` (cubic-bezier(0.42, 0, 0.58, 1)) per segment,
the same 2.5 s cycle. The only difference is that the CSS `transform-origin`
maths is done here in pixels.

Outputs (assets/mascot/):
  mascot-wave-<w>.gif     transparent GIF, loop forever, disposal 2
  mascot-wave-<w>.webp    animated WebP, lossless, 8-bit alpha
  mascot-wave-<w>.apng    APNG, 8-bit alpha
  mascot-wave-preview.png contact sheet

Usage:
  python tools/mascot/render_frames.py --width 512
  python tools/mascot/render_frames.py --width 256
  python tools/mascot/render_frames.py --width 512 --sheet
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets" / "mascot"

CYCLE = 2.5          # seconds, one full wave + rest
FPS = 30
BOB_CSS = 3.0        # px at the component's default 200 px width
BOB_REF_W = 200.0
PAD_OUT = 8          # output px of breathing room around the union bbox

# Keyframes, copied from mascot-wave.css.
WAVE = [(0.0, 0.0), (12.0, -20.0), (24.0, 15.0), (36.0, -15.0), (48.0, 0.0), (100.0, 0.0)]
TILT = [(0.0, 0.0), (50.0, 2.5), (100.0, 0.0)]
BOB = [(0.0, 0.0), (50.0, -1.0), (100.0, 0.0)]

NAVY = (0, 7, 26)


# --------------------------------------------------------------------------- #
# timing
# --------------------------------------------------------------------------- #
def _bezier(u: float, x1: float, y1: float, x2: float, y2: float) -> float:
    """y for a given x on a CSS cubic-bezier timing function."""
    lo, hi = 0.0, 1.0
    for _ in range(24):
        t = (lo + hi) / 2.0
        x = 3 * (1 - t) ** 2 * t * x1 + 3 * (1 - t) * t ** 2 * x2 + t ** 3
        if x < u:
            lo = t
        else:
            hi = t
    t = (lo + hi) / 2.0
    return 3 * (1 - t) ** 2 * t * y1 + 3 * (1 - t) * t ** 2 * y2 + t ** 3


_EASE_LUT = [_bezier(i / 1000.0, 0.42, 0.0, 0.58, 1.0) for i in range(1001)]


def ease(u: float) -> float:
    u = min(max(u, 0.0), 1.0)
    return _EASE_LUT[int(round(u * 1000))]


def track(pct: float, keys: list[tuple[float, float]]) -> float:
    """Value of a CSS keyframe track at `pct` percent, ease-in-out per segment."""
    for (p0, v0), (p1, v1) in zip(keys, keys[1:]):
        if pct <= p1:
            if p1 <= p0:
                return v1
            return v0 + (v1 - v0) * ease((pct - p0) / (p1 - p0))
    return keys[-1][1]


def pose(i: int, n: int, bob_px: float) -> tuple[float, float]:
    """(hand rotation in CSS degrees, bob offset in source px) for frame i."""
    pct = 100.0 * i / n
    return track(pct, WAVE) + track(pct, TILT), track(pct, BOB) * bob_px


# --------------------------------------------------------------------------- #
# geometry
# --------------------------------------------------------------------------- #
def rotate_point(x: float, y: float, cx: float, cy: float, deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def union_box(meta: dict, n: int, bob_px: float, ss: int) -> tuple[int, int, int, int]:
    body = Image.open(ASSETS / "body.png").convert("RGBA")
    hand = Image.open(ASSETS / "hand.png").convert("RGBA")
    px, py = meta["pivot"]
    ox, oy = meta["handOffset"]
    pivot = ((ox + px) * ss, (oy + py) * ss)

    bb = body.getbbox()  # alpha bbox of the static body
    x0, y0, x1, y1 = (bb[0] * ss, bb[1] * ss, bb[2] * ss, bb[3] * ss)
    # the body also travels up by up to bob_px
    y0 -= math.ceil(abs(bob_px) * ss)

    hw, hh = hand.width * ss, hand.height * ss
    hx, hy = ox * ss, oy * ss
    for i in range(n):
        ang, _ = pose(i, n, bob_px)
        for cx, cy in ((hx, hy), (hx + hw, hy), (hx + hw, hy + hh), (hx, hy + hh)):
            rx, ry = rotate_point(cx, cy, pivot[0], pivot[1], ang)
            x0, y0, x1, y1 = min(x0, rx), min(y0, ry), max(x1, rx), max(y1, ry)

    return (int(math.floor(x0)), int(math.floor(y0)),
            int(math.ceil(x1)), int(math.ceil(y1)))


# --------------------------------------------------------------------------- #
# render
# --------------------------------------------------------------------------- #
def render_frames(width: int, fps: int, ss: int) -> tuple[list[Image.Image], dict]:
    meta = json.loads((ASSETS / "pivot.json").read_text(encoding="utf-8"))
    cw, ch = meta["canvas"]
    canvas = (cw * ss, ch * ss)

    body = Image.open(ASSETS / "body.png").convert("RGBA")
    hand = Image.open(ASSETS / "hand.png").convert("RGBA")
    body_ss = body.resize(canvas, Image.LANCZOS)
    hand_ss = hand.resize((hand.width * ss, hand.height * ss), Image.LANCZOS)

    ox, oy = meta["handOffset"]
    px, py = meta["pivot"]
    hand_canvas = Image.new("RGBA", canvas, (0, 0, 0, 0))
    hand_canvas.alpha_composite(hand_ss, (ox * ss, oy * ss))
    pivot = ((ox + px) * ss, (oy + py) * ss)

    bob_px = BOB_CSS * cw / BOB_REF_W  # 3 CSS px at 200 wide, in source px
    n = int(round(fps * CYCLE))

    box = union_box(meta, n, bob_px, ss)
    pad = int(round(PAD_OUT * ss * cw / width))
    box = (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)
    box = (max(0, box[0]), max(0, box[1]), min(canvas[0], box[2]), min(canvas[1], box[3]))
    crop_w, crop_h = box[2] - box[0], box[3] - box[1]
    out_h = int(round(crop_h * width / crop_w))

    frames: list[Image.Image] = []
    t0 = time.time()
    for i in range(n):
        ang, bob = pose(i, n, bob_px)
        rotated = hand_canvas.rotate(-ang, resample=Image.BICUBIC, center=pivot,
                                    fillcolor=(0, 0, 0, 0))
        frame = body_ss.copy()
        frame.alpha_composite(rotated)

        k = int(round(bob * ss))
        if k:
            # CSS translateY(+k) moves content down; sample from y - k.
            frame = frame.transform(frame.size, Image.AFFINE, (1, 0, 0, 0, 1, -k),
                                    resample=Image.BICUBIC)

        frame = frame.crop(box).resize((width, out_h), Image.LANCZOS)
        frames.append(frame)

    info = {
        "frames": n,
        "fps": fps,
        "width": width,
        "height": out_h,
        "ss": ss,
        "bob": round(bob_px, 2),
        "crop": box,
        "seconds": round(time.time() - t0, 2),
    }
    return frames, info


# --------------------------------------------------------------------------- #
# writers
# --------------------------------------------------------------------------- #
def delays(n: int, total: int) -> list[int]:
    """n per-frame delays summing to `total` (spread so the error never drifts)."""
    edges = [int(round((i + 1) * total / n)) for i in range(n)]
    prev = 0
    out = []
    for e in edges:
        out.append(e - prev)
        prev = e
    return out


def write_gif(frames: list[Image.Image], path: Path, colors: int) -> dict:
    """One global palette, last index reserved for transparency, disposal 2."""
    step = max(1, len(frames) // 8)
    picks = frames[::step]
    montage = Image.new("RGB", (frames[0].width, frames[0].height * len(picks)), NAVY)
    for j, f in enumerate(picks):
        flat = Image.new("RGB", f.size, NAVY)
        flat.paste(f, (0, 0), f)
        montage.paste(flat, (0, j * f.height))

    idx = colors - 1
    quant = montage.quantize(colors=idx, method=Image.MEDIANCUT, dither=Image.NONE)
    palette = quant.getpalette()[: idx * 3] + list(NAVY)  # last entry: transparent
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette(palette)

    p_frames = []
    hole_index = colors - 1
    for f in frames:
        flat = Image.new("RGB", f.size, NAVY)
        flat.paste(f, (0, 0), f)
        p = flat.quantize(palette=pal_img, dither=Image.NONE)
        hole = f.getchannel("A").point(lambda v: 255 if v < 128 else 0)
        p.paste(Image.new("P", p.size, hole_index), (0, 0), hole)
        p.info["transparency"] = hole_index
        p_frames.append(p)

    p_frames[0].save(
        path,
        save_all=True,
        append_images=p_frames[1:],
        duration=[c * 10 for c in delays(len(frames), int(round(CYCLE * 100)))],
        loop=0,
        disposal=2,
        optimize=True,
        transparency=hole_index,
    )
    return {"colors": colors, "transparent_index": hole_index}


def write_webp(frames: list[Image.Image], path: Path) -> None:
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=delays(len(frames), int(round(CYCLE * 1000))),  # milliseconds
        loop=0,
        lossless=True,
        quality=100,
        method=4,
        minimize_size=False,
    )


def write_apng(frames: list[Image.Image], path: Path) -> None:
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=delays(len(frames), int(round(CYCLE * 1000))),  # milliseconds
        loop=0,
        disposal=1,
        blend=0,
        optimize=False,
    )


def contact_sheet(frames: list[Image.Image], path: Path) -> None:
    picks = [0, 9, 18, 27, 36, 60]
    tw = frames[0].width
    th = frames[0].height
    cols, rows = 3, 2
    gap, cap = 12, 18
    sheet = Image.new("RGBA", (cols * tw + (cols + 1) * gap,
                              rows * (th + cap) + (rows + 1) * gap),
                      (241, 241, 242, 255))
    draw = ImageDraw.Draw(sheet)
    for k, idx in enumerate(picks):
        r, c = divmod(k, cols)
        x = gap + c * (tw + gap)
        y = gap + r * (th + cap + gap)
        cell = Image.new("RGBA", (tw, th), (255, 255, 255, 255))
        cell.alpha_composite(frames[idx])
        sheet.alpha_composite(cell, (x, y))
        ang, _ = pose(idx, len(frames), 1.0)
        draw.text((x + 2, y + th + 3), f"frame {idx:02d}  {ang:+.1f}deg", fill=(90, 94, 100, 255))
    sheet.convert("RGB").save(path)


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=512)
    ap.add_argument("--fps", type=int, default=FPS)
    ap.add_argument("--ss", type=int, default=2, help="supersample factor")
    ap.add_argument("--colors", type=int, default=255, help="GIF palette size (max 256)")
    ap.add_argument("--sheet", action="store_true", help="also write the contact sheet")
    args = ap.parse_args()

    frames, info = render_frames(args.width, args.fps, args.ss)
    if args.width == 512:
        stem = ASSETS / "mascot-wave"
    else:
        stem = ASSETS / f"mascot-wave-{args.width}"

    print(f"rendered {info['frames']} frames in {info['seconds']}s "
          f"-> {info['width']}x{info['height']} (ss={info['ss']}, bob={info['bob']}px)")

    write_gif(frames, stem.with_suffix(".gif"), args.colors)
    write_webp(frames, stem.with_suffix(".webp"))
    write_apng(frames, stem.with_suffix(".apng"))
    if args.sheet or args.width == 512:
        contact_sheet(frames, ASSETS / "mascot-wave-preview.png")

    for ext in ("gif", "webp", "apng"):
        p = stem.with_suffix("." + ext)
        print(f"  {p.name:24} {p.stat().st_size / 1024:9.1f} KiB")
    if args.sheet or args.width == 512:
        p = ASSETS / "mascot-wave-preview.png"
        print(f"  {p.name:24} {p.stat().st_size / 1024:9.1f} KiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
