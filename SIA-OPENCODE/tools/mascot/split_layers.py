"""Split the Loc8 mascot into a static body and a rotating hand layer.

Outputs (assets/mascot/):
  body.png    full mascot, hand removed and the wrist/cheek/ear repainted
  hand.png    the waving glove + its navy outline, transparent
  pivot.json  wrist pivot (hand.png pixels) + hand offset on the shared canvas

Run:  python tools/mascot/split_layers.py [--debug]
"""

from __future__ import annotations

import json
import math
import sys
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "Reference" / "mascotHome.png"
OUT = ROOT / "assets" / "mascot"

# Palette sampled from the artwork (never invented).
NAVY = (0, 7, 26)
WHITE = (255, 255, 255)
LAVENDER = (205, 205, 231)

# Outline stroke width of the mascot, measured from the art (~20 px).
STROKE = 20.0

# All geometry runs in this window: it contains the glove and every body part
# the glove touches. Keeps the exact distance transforms affordable.
WIN = (770, 480, 1190, 910)

# Flood seeds: one pixel safely inside each flat-colour region.
SEEDS = {
    "palm": (980, 690),
    "cuff": (920, 790),
    "head": (850, 600),
    "ear": (995, 560),
    "hoodie": (860, 760),
}


def light(px) -> bool:
    return px[3] > 128 and int(px[0]) + int(px[1]) + int(px[2]) > 450


def blue(px) -> bool:
    return px[3] > 128 and px[2] > 70 and px[0] < 90


def flood(arr: np.ndarray, seed: tuple[int, int], pred) -> np.ndarray:
    h, w = arr.shape[:2]
    vis = np.zeros((h, w), bool)
    sx, sy = seed
    if not pred(arr[sy, sx]):
        raise ValueError(f"seed {seed} is not in the target region: {arr[sy, sx]}")
    vis[sy, sx] = True
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not vis[ny, nx] and pred(arr[ny, nx]):
                vis[ny, nx] = True
                q.append((nx, ny))
    return vis


def edt(mask: np.ndarray) -> np.ndarray:
    """Exact Euclidean distance to the nearest True pixel (Felzenszwalb)."""
    inf = 1e9
    f = np.where(mask, 0.0, inf)

    def one_d(g: np.ndarray) -> np.ndarray:
        n = g.shape[0]
        d = np.empty_like(g)
        v = np.zeros(n, np.int32)
        z = np.zeros(n + 1)
        for j in range(g.shape[1]):
            col = g[:, j]
            k = 0
            v[0] = 0
            z[0] = -inf
            z[1] = inf
            for q in range(1, n):
                s = ((col[q] + q * q) - (col[v[k]] + v[k] * v[k])) / (2.0 * q - 2.0 * v[k])
                while s <= z[k]:
                    k -= 1
                    s = ((col[q] + q * q) - (col[v[k]] + v[k] * v[k])) / (2.0 * q - 2.0 * v[k])
                k += 1
                v[k] = q
                z[k] = s
                z[k + 1] = inf
            k = 0
            for q in range(n):
                while z[k + 1] < q:
                    k += 1
                dx = q - v[k]
                d[q, j] = dx * dx + col[v[k]]
        return d

    return np.sqrt(one_d(one_d(f).T).T)


def dilate(mask: np.ndarray, radius: float) -> np.ndarray:
    return edt(mask) <= radius


def fit_ellipse(mask: np.ndarray) -> tuple[float, float, float, float, float]:
    """Moment-based ellipse fit. Returns (cx, cy, a, b, angle_rad)."""
    ys, xs = np.nonzero(mask)
    cx, cy = xs.mean(), ys.mean()
    x = xs - cx
    y = ys - cy
    mxx, myy, mxy = (x * x).mean(), (y * y).mean(), (x * y).mean()
    common = math.sqrt((mxx - myy) ** 2 + 4 * mxy ** 2)
    a = 2.0 * math.sqrt(max(mxx + myy + common, 1e-9))
    b = 2.0 * math.sqrt(max(mxx + myy - common, 1e-9))
    ang = 0.5 * math.atan2(2 * mxy, mxx - myy)
    return cx, cy, a, b, ang


def wrist_pivot(palm: np.ndarray, cuff: np.ndarray) -> tuple[float, float]:
    """Centre of the wrist crease: the ridge where palm and cuff are equidistant."""
    dp = edt(palm)
    dc = edt(cuff)
    ridge = (np.abs(dp - dc) <= 1.0) & (dp < 26) & (dc < 26) & ~palm & ~cuff
    if not ridge.any():
        raise RuntimeError("could not locate the wrist crease")
    ys, xs = np.nonzero(ridge)
    return float(xs.mean()), float(ys.mean())


def fit_circle(pts: np.ndarray) -> tuple[float, float, float]:
    """Least-squares circle through points, with one outlier rejection pass."""
    def solve(p):
        x, y = p[:, 0], p[:, 1]
        a = np.c_[2 * x, 2 * y, np.ones(len(x))]
        b = x * x + y * y
        sol, *_ = np.linalg.lstsq(a, b, rcond=None)
        cx, cy = sol[0], sol[1]
        return cx, cy, math.sqrt(max(sol[2] + cx * cx + cy * cy, 1e-9))

    cx, cy, r = solve(pts)
    d = np.hypot(pts[:, 0] - cx, pts[:, 1] - cy)
    inl = np.abs(d - r) < 3.5
    if inl.sum() > 20:
        cx, cy, r = solve(pts[inl])
    return cx, cy, r


def boundary(mask: np.ndarray) -> np.ndarray:
    return mask & ~erode(mask, 1)


def erode(mask: np.ndarray, radius: float) -> np.ndarray:
    return ~dilate(~mask, radius)


def main() -> int:
    debug = "--debug" in sys.argv
    src = Image.open(SRC).convert("RGBA")
    arr = np.array(src)
    h, w = arr.shape[:2]

    print("flood-filling colour regions ...")
    cores_full = {name: flood(arr, seed, light) for name, seed in SEEDS.items() if name != "hoodie"}
    cores_full["hoodie"] = flood(arr, SEEDS["hoodie"], blue)

    wx0, wy0, wx1, wy1 = WIN
    sub = arr[wy0:wy1, wx0:wx1]
    cores = {k: v[wy0:wy1, wx0:wx1] for k, v in cores_full.items()}
    alpha = sub[:, :, 3] > 0
    print(f"window {sub.shape[1]}x{sub.shape[0]}")

    palm = cores["palm"]
    d_palm = edt(palm)

    # --- hand mask: the glove plus its own navy outline ---------------------
    print("building hand mask ...")
    hand_core = (d_palm <= 24.0) & alpha
    for name in ("head", "ear", "cuff", "hoodie"):
        hand_core &= ~(edt(cores[name]) <= 1.0)

    # --- body silhouette: offset every body part's core by the stroke width -
    print("rebuilding the body silhouette ...")
    core_union = np.zeros_like(hand_core)
    for c in cores.values():
        core_union |= edt(c) <= 2.0

    restored = np.zeros_like(hand_core)
    for name in ("head", "ear", "cuff", "hoodie"):
        d = edt(cores[name])
        restored |= (d <= STROKE + 5.0) & (d > 1.5)
    restored &= alpha
    # Bridge the sleeve/arm junction: the cuff and the hoodie are one silhouette
    # there, and the glove sat across the seam between them.
    restored |= (edt(cores["cuff"]) <= 45) & (edt(cores["hoodie"]) <= 45) & alpha
    # Never paint outline over a flat-colour interior.
    restored &= ~core_union
    patch = restored & hand_core

    # --- wrist stub ---------------------------------------------------------
    # The hand also carries a thin cuff-coloured overlap so the join cannot open
    # up when it rotates. The body keeps those pixels too: white over white.
    stub = (edt(hand_core) <= 14.0) & (edt(cores["cuff"]) <= 8.0) & alpha
    stub &= ~hand_core
    hand = hand_core | stub

    # --- interior completion ------------------------------------------------
    # The glove covered nothing but navy outline: the headphone's white sliver,
    # the cuff's white and the ear rim are all capped by `restored` above, which
    # reads as the sleeve opening and the headphone edge once the hand rotates.
    ear_fill = np.zeros_like(hand)
    ear_ring = np.zeros_like(hand)

    # Cuff: the white sleeve is a circular band cut off by the palm. Its own
    # outline is restored by `restored`, which caps it as a sleeve opening.

    # --- paint ---------------------------------------------------------------
    body = sub.copy()
    # Clear the glove, plus the soft fringe it left along its own outline.
    fringe = (sub[:, :, 3] > 0) & (sub[:, :, 3] < 255) & (d_palm <= 30)
    body[hand_core | fringe] = 0
    # The body's outline, restored where the glove sat on top of it. This is the
    # head's cheek edge, the cuff's cap and the ear's rim.
    body[restored & hand] = (*NAVY, 255)
    # Completed ear cup (rim + interior).
    body[ear_ring] = (*NAVY, 255)
    body[ear_fill] = (*LAVENDER, 255)

    hand_px = np.zeros_like(sub)
    hand_px[hand] = sub[hand]

    if debug:
        _debug(sub, body, hand_px, patch, ear_fill, ear_ring)

    # --- stitch back into the full canvas ------------------------------------
    body_full = arr.copy()
    body_full[wy0:wy1, wx0:wx1] = body
    hand_full_arr = np.zeros_like(arr)
    hand_full_arr[wy0:wy1, wx0:wx1] = hand_px

    # --- crop to a shared canvas --------------------------------------------
    bb = Image.fromarray(((arr[:, :, 3] > 0) * 255).astype(np.uint8)).getbbox()
    pad = 20
    cx0, cy0 = max(0, bb[0] - pad), max(0, bb[1] - pad)
    cx1, cy1 = min(w, bb[2] + pad), min(h, bb[3] + pad)

    body_img = Image.fromarray(body_full).crop((cx0, cy0, cx1, cy1))
    hand_canvas = Image.fromarray(hand_full_arr).crop((cx0, cy0, cx1, cy1))
    hb = hand_canvas.getbbox()
    hpad = 6
    hx0, hy0 = max(0, hb[0] - hpad), max(0, hb[1] - hpad)
    hx1, hy1 = min(hand_canvas.width, hb[2] + hpad), min(hand_canvas.height, hb[3] + hpad)
    hand_img = hand_canvas.crop((hx0, hy0, hx1, hy1))

    px, py = wrist_pivot(cores["palm"], cores["cuff"])
    pivot = (px + wx0 - cx0 - hx0, py + wy0 - cy0 - hy0)

    OUT.mkdir(parents=True, exist_ok=True)
    body_img.save(OUT / "body.png")
    hand_img.save(OUT / "hand.png")
    (OUT / "pivot.json").write_text(json.dumps({
        "pivot": [round(pivot[0], 1), round(pivot[1], 1)],
        "handSize": [hand_img.width, hand_img.height],
        "handOffset": [hx0, hy0],
        "canvas": [body_img.width, body_img.height],
        "source": {"file": "Reference/mascotHome.png", "crop": [cx0, cy0, cx1, cy1]},
        "stroke": STROKE,
    }, indent=2) + "\n", encoding="utf-8")

    # --- checks -------------------------------------------------------------
    comp = body_img.copy()
    comp.paste(hand_img, (hx0, hy0), hand_img)
    ref = src.crop((cx0, cy0, cx1, cy1))
    diff = np.abs(np.asarray(comp, np.int32) - np.asarray(ref, np.int32))
    opaque = np.asarray(ref)[:, :, 3] > 0
    print()
    print(f"canvas    {body_img.width}x{body_img.height}")
    print(f"hand      {hand_img.width}x{hand_img.height} @ {hx0},{hy0}")
    print(f"pivot     {pivot[0]:.1f},{pivot[1]:.1f} (hand.png px)")
    print(f"rest diff max={diff[opaque].max()}  mean={diff[opaque].mean():.4f}")
    return 0


def _debug(sub, body, hand_px, patch, ear_fill, ear_ring) -> None:
    tmp = OUT / "_debug"
    tmp.mkdir(parents=True, exist_ok=True)
    overlay = sub.copy()
    overlay[patch] = (255, 0, 255, 255)
    overlay[ear_ring] = (255, 140, 0, 255)
    overlay[ear_fill] = (0, 255, 0, 255)
    for name, img in (
        ("1_body", Image.fromarray(body)),
        ("2_hand", Image.fromarray(hand_px)),
        ("3_patch", Image.fromarray(overlay)),
    ):
        img.resize((img.width * 2, img.height * 2), Image.NEAREST).save(tmp / f"{name}.png")
    print(f"debug crops -> {tmp}")


if __name__ == "__main__":
    raise SystemExit(main())
