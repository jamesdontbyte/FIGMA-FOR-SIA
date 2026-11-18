# Role/Commuter/NearestJeepney: full spec

> Detail file for `DESIGN.md` section 11. Tokens and hard rules come from `DESIGN.md`; this file holds only this card's anatomy, variants and motion.

**Role/Commuter/NearestJeepney anatomy and motion** — 361 wide, prop/state driven (`setEta(n)`, `setSeats(array, capacity)`, `selectRoute(id)`, `setAlert(bool)`). The executable reference for all motion is **HTML prototype not yet in the repo**. Header is `Role/Commuter/CardHeader` (`Tone=Live`, title `Nearest jeepney`, meta `5 ACTIVE · LIVE · 20S`); below it a route tab row in the order `R1 · Bugasong`, `R3 · Patnongon`, `R2 · San Jose` (display order only, route codes unchanged), styled like the Fare card tabs: text buttons with one `Indicator` line (`size/tab-underline` 2 px `primary/default` filled bar, `radius/pill`, no pill behind the label) that slides and resizes under the selected route, active label `text/primary`, inactive `text/secondary`; then the ETA (`type/display` 40/48 weight 800 number + `MIN` in `type/mono-tag`), the sub line (`J-014 · arriving Plaza` in `type/mono-body`), the 20-dot seat grid (`size/dot-sm` 8 px dots, 10 per row, `space/2` 8 px gap — free = dark `text/primary`, taken = light gray `bg/strong`), the count line (`8 of 20 seats free`) and the freshness line (`DRIVER-REPORTED · 2 MIN AGO`), then the action row: `Button/Primary` "Track Jeepney" + `Button/Secondary` "Alert me" in an `Alert Slot`.

| Variant | Size | Shows |
|---|---|---|
| `State=Live, Route=R1/R2/R3, Alert on=Off/On` | 361 × 320 | Full card per route (`R1`: ETA 6, `J-014 · arriving Plaza`, 8/20 free; `R2`: ETA 3, `J-021 · arriving San Jose`, 12/20 free; `R3`: ETA 11, `J-007 · arriving Market`, 0/20 `Full`), wired with Smart Animate between routes and alert states |
| `State=Arriving, Route=R1, Alert on=Off` | 361 × 298 | ETA slot reads `Arriving` (`type/h3` 18/26 SemiBold, ETA under 1 min), unit label hidden |
| `State=Full, Route=R1, Alert on=Off` | 361 × 320 | Count line reads `Full` (0 free seats), every seat dot in `bg/strong` |
| `State=No jeepneys, Route=R1, Alert on=Off` | 361 × 188 | Chips stay, body copy "No jeepneys on this route right now", `Track Jeepney` disabled, alert still available |
| `State=Loading, Route=R1, Alert on=Off` | 361 × 320 | `bg/muted` skeletons in every slot, header title `Nearest jeepney` retained |
| `State=Pressed Track / Pressed Alert` | 361 × 320 | `WHILE_PRESSING` (`ON_PRESS`) target scaling `Button/Track` or `Alert Slot` to 97 % over 150 ms |

`Alert on=On` swaps the secondary alert button for an absolutely positioned `Alert On Layer` (145 × 40, `bg/muted`, no stroke, `Icon/bell` + "Alerts on") sitting above it inside `Alert Slot`, so the old button never shows through. Seat counts are always the driver's last entry, capped at 20 dots; ETA under 1 min becomes `Arriving`; long route labels truncate with an ENDING ellipsis and never wrap the chip row. With only 3 routes, the chip row always fits and does not scroll.

**Motion specification** (HTML reference: HTML prototype not yet in the repo; Figma prototype runs `Foundations/LivePulse`, `Foundations/ETACountdown`, `Foundations/SeatsLive`, route chip slide, alert toggle, and button press states via Smart Animate):

| Element / Transition | Duration & Delay | Easing | Keyframes / Values |
|---|---|---|---|
| Card section rise-in (`.rise`) | `--enter-dur: 500ms`, delay `calc(70ms * var(--i))` (`--i: 0..4`) | `cubic-bezier(0.22, 1, 0.36, 1)` (`--ease-smooth-out`) | From `opacity: 0; transform: translateY(8px); filter: blur(2px)` → resting state |
| Live status dot pulse (`.live::after`) | `--pulse-dur: 2000ms`, infinite | `cubic-bezier(0.22, 1, 0.36, 1)` | `0%: scale(1), opacity: 0.5` → `70%, 100%: scale(2.6), opacity: 0` |
| Route chip indicator slide (`.chip-ind`) | `--tab-dur: 250ms` | `cubic-bezier(0.22, 1, 0.36, 1)` (`--tab-ease`) | Animates `transform: translateX(...)` and `width` to match active chip; chip text color transitions in `250ms` |
| ETA & seat-count digit roll (`t-digit-in` / `t-digit-out`) | In: `--digit-dur: 600ms`, delay `calc(40ms * var(--digit-i, 0) + 50ms)`; Out: `--digit-exit-dur: 155ms`, delay `calc(40ms * var(--digit-i, 0))` | `linear` (spring curve baked into 21 keyframe steps) | `--digit-distance: 0.52em`, `--digit-exit-distance: 0.52em`, `--digit-lift: 0.125em`, `--digit-start-scale: 0.7`, `--digit-peak: 1.03`, `--digit-blur: max(0.067em, 0.171em - 2.1px)`. Unchanged leading digits get `[data-same]` (`animation: none`), so on `10 → 11` only the ones digit rolls, and on `10 → 9` the single changed slot rolls with outgoing `0` and incoming `9` |
| Sub line crossfade (`.t-soft`) | `--soft-dur: 200ms` | `ease-in-out` | Exit: `opacity: 0; filter: blur(2px)` (`--soft-blur`), swaps text at `200ms`, then fades back in |
| Seat dots intro & change (`.dot`) | Fill: `--dot-dur: 250ms`; Intro: `300ms`, delay `calc(400ms + 30ms * var(--n))`; Pop: `250ms` | `cubic-bezier(0.22, 1, 0.36, 1)` | Intro `dot-in`: `from { opacity: 0; transform: scale(0) }`; Changed dot `dot-pop`: `40% { transform: scale(1.6) }` (`--dot-pop: 1.6`). Only dots whose boolean state changed pop |
| Count / `Full` & ETA / `Arriving` text swap (`.t-text-swap`) | `--text-swap-dur: 150ms` | `ease-in-out` (`--text-swap-ease`) | Exit (`.is-exit`): `translateY(-4px)`, `filter: blur(2px)`, `opacity: 0` |
| Button & chip press (`.btn`, `.chip`) | `--press-dur: 150ms` (touch hold enforces minimum `150ms` press visibility) | `cubic-bezier(0.22, 1, 0.36, 1)` | `transform: scale(0.97)` (`--press-scale: 0.97`); `Alert me` ↔ `Alerts on` swaps in `150ms` |
| Reduced motion (`prefers-reduced-motion: reduce`) | `0ms` (instant) | `none` | Disables `.rise`, `.live::after`, `.dot.is-intro`, `.dot.is-changed`, `.t-digit` animations, hides `.t-digit-old`, and removes transitions/press scale |

Accessibility: `aria-pressed` on route chips and the alert toggle, `role="img"` with a dynamic `aria-label` (`"N of M seats free"`) on the seat dots grid, `aria-live="polite"` on the ETA and `Arriving` line, visible focus states (fill change, no outline), 44 px minimum touch hit areas on chips and buttons, and no reliance on seat-dot color alone (the count line carries the meaning).

Clash notes — where the prototype and DESIGN.md disagreed, DESIGN.md won:
1. ETA is 60/70 px in the prototype; here it is `type/display` (40/48, weight 800) so the card clears the 361 grid.
2. Card padding 24 px becomes `space/4` 16 px and internal card row gap 24 px becomes `space/4` 16 px, matching `FlatCard` and the other Home cards.
3. The prototype's lowercase "min" unit becomes `MIN` in `type/mono-tag`.
4. The title row is `Role/Commuter/CardHeader`, so the prototype's separate "5 active" counter is folded into its meta string as `5 ACTIVE · LIVE · 20S` (uppercase mono per `type/mono-tag`).
5. Prototype buttons (36 px, 20 px radius) become the shared `Button/Primary` / `Button/Secondary` Small (40 px, `radius/pill`).
6. Seat dots use free = dark (`text/primary`) and taken = light gray (`bg/strong`) across both `Role/Commuter/NearestJeepney` and `Card/Jeepney`.
7. The alert on-state uses `bg/muted` + "Alerts on" rather than the prototype's accent-filled toggle, because `accent` is reserved for live/go/location and the filled black button is already spent on `Track Jeepney`.
8. Any border, outline or gradient in the prototype is removed; surfaces use flat fill, radius and shadow.
