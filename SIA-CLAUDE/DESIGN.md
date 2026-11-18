# DESIGN.md: Loc8 Design System

> App name: **Loc8**. Logo: TBD — use `[APP LOGO]` placeholder until final.
> Product: Loc8, a jeepney tracking app with two roles, **Commuter** and **Driver**. A coop/LTFRB/LTO web dashboard comes later and reuses the color, type and spacing tokens (the no-border, flat-fill-by-default and no-header rules below apply to the mobile app).

## 0. How to use this file (agents read this first)

- Every component, screen and page MUST use the tokens below. **Never hard-code hex values, font sizes, radii or spacing.**
- **Reuse first.** Use components and assets listed in section 11. Create a new one only when the user explicitly asks.
- If a needed token or component is missing, add it to this file first, then use it.
- Style in one line: **soft minimalist**. White canvas, pastel tints, pill shapes, black primary actions, very little text, visuals first.
- **Hard rules for the mobile app (never break these):**
  1. **No borders, strokes or outlines on any UI element.** Shape comes from fill, radius and shadow only. Keep all border radius values. Map drawings (road casing, route line, marker focus halo, origin pin) are not UI elements and may use strokes (see 2.6).
  2. **No header or top bar.** Screens start directly with content. The only hero area is the auth hero on Login and Sign Up. The only title row is `PageHead` on the full-screen inner pages: the plus-menu pages (Start waiting, Chat) and the History inner pages (Trip details, Report issue), see 6.4.
  3. **Flat fills by default. Gradients only on request.** Every fill is a flat color unless the user explicitly asks for a gradient on a specific component. Never add a gradient on your own, and do not spread an existing gradient to other components. Approved gradient components so far: the weather card (`Role/Commuter/WeatherCard`), using the `weather/*` tokens in 2.7. When the user requests a new one, add its tokens to 2.7 and list it here.
  4. **Only 3 routes:** Bugasong, San Jose, Patnongon.
- Platform-agnostic: tokens are named for Figma variables and map to any stack.
- Both roles share the same system.

## 1. Principles

1. **Clean, not cluttered.** One focal point per screen, at most 3 to 4 cards above the fold.
2. **Visuals over text.** Numbers, icons, rings, and color chips instead of sentences. One short label per card.
3. **Soft and rounded.** Large radii, light shadows, flat pastel fills. No borders. Flat fills, with gradients only where the user asked for them (see 2.7).
4. **One black action.** One filled black button per view. Everything else is quieter. Exception: the weather pill and weather card use the charcoal `bg/mascot-band`; they show status, not an action, so they do not count.
5. **Honest status.** Live, stale and offline states are always visible and never rely on color alone.
6. **Glanceable.** Key values (ETA, seats, status) are the largest thing in their card.

## 2. Color

### 2.1 Core

| Token | Hex | Use |
|---|---|---|
| `bg/default` | `#FFFFFF` | Card and control surface |
| `bg/app` | `#F9FAFC` | Near-white, slightly cool screen canvas background |
| `bg/subtle` | `#F7F8FA` | Grouped sections, page behind cards when needed |
| `bg/muted` | `#F1F3F6` | Inputs, select fields, secondary buttons, segmented control track |
| `bg/strong` | `#D3D8DF` | Flat fills only: sheet handle, inactive page dot, switch off track, taken seat dots |
| `bg/auth-hero` | `#0A0A0A` | App-ink hero behind auth sheets (Login / Sign Up). Figma alias of `primary/default`, so it follows that token automatically |
| `bg/mascot-band` | `#262B35` | Light-black / charcoal band behind the mascot hero on Home and History (`Role/Commuter/MascotHero`). Figma alias of `primary/pressed` |
| `text/primary` | `#0F1115` | Headings, values |
| `text/secondary` | `#5F6877` | Labels, captions |
| `text/tertiary` | `#8A92A0` | Placeholders, hints (never for essential info) |
| `text/inverse` | `#FFFFFF` | Text on black or accent |
| `text/on-hero-subtle` | `#CDE6FA` | Subtitle text on the auth hero |
| `primary/default` | `#0A0A0A` | **Primary button**, active nav tab, selected segment |
| `primary/pressed` | `#262B35` | Primary pressed |
| `primary/disabled` | `#D3D8DF` | Disabled fill (text `text/tertiary`) |

There are **no border tokens**. Do not add `border/*` tokens.

### 2.2 Accent (blue)

| Token | Hex | Use |
|---|---|---|
| `accent/default` | `#1F6FEB` | Floating action button, links, progress, user location, `cta-button` |
| `accent/pressed` | `#1859C2` | Pressed |
| `accent/tint` | `#E8F1FE` | Accent chips, selected-row backgrounds, focused input fill |

Use the accent sparingly. Black carries actions, blue carries "live / go / you are here."

### 2.3 Pastel card tints (category cards, stat tiles, illustrations)

| Name | Fill Token | Fill Hex | Ink Token | Ink Hex (icon/ring/number accent) |
|---|---|---|---|---|
| Sky | `tint/sky-fill` | `#E1EFFB` | `tint/sky-ink` | `#1F6FEB` |
| Lavender | `tint/lavender-fill` | `#EDE7F8` | `tint/lavender-ink` | `#6B4FB3` |
| Mint | `tint/mint-fill` | `#DFF3E4` | `tint/mint-ink` | `#2E8B57` |
| Peach | `tint/peach-fill` | `#FDE9DF` | `tint/peach-ink` | `#D2622B` |
| Butter | `tint/butter-fill` | `#FFF4CF` | `tint/butter-ink` | `#A87A00` |
| Lime (highlight) | `tint/lime-fill` | `#E2F5B8` | `tint/lime-ink` | `#4F7A12` |

Rules: one tint per card, never two tints in the same card. Tinted cards have no shadow and no border. Max 3 tints visible per screen.

### 2.4 Semantic

| Role | Fill Token | Fill Hex | Ink Token | Ink Hex |
|---|---|---|---|---|
| Success | `semantic/success-fill` | `#E3F5EA` | `semantic/success-ink` | `#1E8E4F` |
| Warning | `semantic/warning-fill` | `#FFF4D6` | `semantic/warning-ink` | `#9A6700` |
| Error | `semantic/error-fill` | `#FDECEC` | `semantic/error-ink` | `#D93036` |
| Info | `semantic/info-fill` | `#E8F1FE` | `semantic/info-ink` | `#1F6FEB` |

### 2.5 App-specific colors

| Token | Hex | Use |
|---|---|---|
| `status/live` | `#2E9E5B` | GPS live, fresh location |
| `status/weak` | `#F5A524` | Weak or delayed GPS |
| `status/lost` | `#E5484D` | GPS lost |
| `status/stale` | `#8A92A0` | Offline or stale marker (50% opacity) |
| `demand/low` | `#4CC38A` | Heatmap and hotspot level 1 |
| `demand/medium` | `#F5C542` | Level 2 |
| `demand/high` | `#F28C38` | Level 3 |
| `demand/peak` | `#E5484D` | Highest demand |
| `route/1` to `route/3` | `#1F6FEB` `#F28C38` `#2E9E5B` | **Only 3 routes**, one color each: `R1 · Bugasong` (`route/1`), `R2 · San Jose` (`route/2`), `R3 · Patnongon` (`route/3`). Never red (reserved for errors). Do not add more routes or route colors. |

### 2.6 Map palette (base map surfaces)

| Token | Hex | Use |
|---|---|---|
| `map/water` | `#D9E8F5` | Open sea and deep water on the base map |
| `map/water-shallow` | `#E7F1FA` | Flat coastal shelf band along the shoreline and estuaries |
| `map/land` | `#F7F4EA` | Land mass fill |
| `map/landcover` | `#E8F0E1` | Flat vegetation and inland terrace patches |
| `map/road-casing` | `#E2DED2` | Casing behind base-map roads (the road core is `bg/default`) |

Rules: base-map surfaces only — never on cards, buttons, chips or nav. All map fills are flat, no gradients. One road per map, no labels, no POIs, no pins, no route line. A screen that needs a route draws it above `Map/Base`. The road casing, route line, marker focus halo and origin pin are map drawings, not UI borders, so they may use strokes.

### 2.7 Gradient tokens (user-requested components only)

Gradients exist only on components the user explicitly asked to have one. Right now that is the weather card (`Role/Commuter/WeatherCard`). Never use these tokens on any other surface.

| Token | Value | Use |
|---|---|---|
| `weather/sky-clear` | `linear 180° #1F63C4 → #2A72D2 (55%) → #2F7AD6` | Sunny sky |
| `weather/sky-cloudy` | `linear 180° #455E79 → #637A92` | Cloudy sky |
| `weather/sky-rain` | `linear 180° #3A4B5E → #56697D` | Rain sky |
| `weather/sky-storm` | `linear 180° #2E3641 → #4D5866` | Storm sky |
| `weather/glow-warm` · `glow-cool` · `glow-cloud` · `glow-mist` · `glow-storm` | `rgba(255,200,120,.34)` · `rgba(110,190,255,.32)` · `rgba(255,255,255,.18)` · `rgba(170,200,230,.22)` · `rgba(140,160,190,.20)` | Soft radial light that drifts over the sky (clear: warm + cool, cloudy: cloud, rain: mist, storm: storm) |
| `weather/rain` | `rgba(255,255,255,0.42)` | Rain streaks (rain and storm) |
| `weather/flash` | `rgba(255,255,255,0.50)` | Lightning flash (storm only) |
| `weather/text-muted` | `rgba(255,255,255,0.88)` | Day name, H/L line and inactive tab labels on the sky |
| `weather/tab-track` | `rgba(0,0,0,0.16)` | Day tab track |
| `weather/tab-pill` | `rgba(255,255,255,0.20)` | Selected day pill (focus: `rgba(255,255,255,0.32)`; inactive tab focus: `rgba(255,255,255,0.12)`) |
| `weather/sun` | `#FFD75E` | Sun and bolt icons, and the sun in `Icon/cloud-sun`. Figma color variable `weather/sun` |

Rules: main text on the sky is `text/inverse`. The sky gradients are slightly darker than the transitions.dev reference so white text stays readable. Cross-fade between skies, never animate the gradient itself.

## 3. Typography

**Font family: Plus Jakarta Sans** (weights 400, 500, 600, 700, 800) for all text. **Exception:** `JetBrains Mono` (weight 500) is used only by `type/mono-tag` and `type/mono-body`. No other fonts. Fallback: system sans-serif (system monospace for the mono styles). Support OS font scaling up to 130%.

These are Figma **text styles**, not variables.

| Token | Size / Line | Weight | Use |
|---|---|---|---|
| `type/display` | 40 / 48 | 800 | Big numbers (ETA, counters) |
| `type/h1` | 28 / 36 | 700 | Screen titles, hero line |
| `type/h2` | 22 / 30 | 700 | Section titles |
| `type/h3` | 18 / 26 | 600 | Card titles |
| `type/body-lg` | 16 / 24 | 500 | Primary body, buttons |
| `type/body` | 14 / 20 | 400 | Secondary text |
| `type/caption` | 12 / 16 | 500 | Labels, chips, timestamps, card header titles |
| `type/overline` | 11 / 14 | 600, +4% tracking | Tiny uppercase tags (rare) |
| `type/greeting` | 17 / 24 | 600 | Home greeting title (`"Good morning, Ana"`) |
| `type/weather-temp` | 60 / 70 | 500, -2% tracking | Weather card temperature only |
| `type/mono-tag` | 10 / 14 | 500 (`JetBrains Mono`), +4% tracking | Monospace dates (`"TODAY, 11 NOVEMBER"`), secondary telemetry (`"LIVE · 20S AGO"`, `"DRIVER-REPORTED · 2 MIN AGO"`), and units (`"MIN"`) |
| `type/mono-body` | 11 / 15 | 500 (`JetBrains Mono`) | Monospace seat counts and compact status lines (`"8 of 16 seats free"`, `"J-014 · arriving Plaza"`) |

Rules:
- Max 2 weights per card. Values use 700 or 800, labels use 500.
- Units sit next to the number at `type/body` in `text/secondary` (for example **6** min, **28**°C).
- Sentence case everywhere. No all-caps buttons.
- Keep copy short: titles 1 to 3 words, helper text one line.
- Every text layer uses one of the styles above. Do not set a font size by hand.

## 4. Layout, spacing, shape

### 4.1 Spacing (4pt grid) & Layout Constants

`space/0`=0 · `space/1`=4 · `space/2`=8 · `space/3`=12 · `space/4`=16 · `space/5`=20 · `space/6`=24 · `space/8`=32 · `space/10`=40 · `space/12`=48 · `space/14`=56 · `space/16`=64 · `space/20`=80

**Spec & Layout Tokens (in Spacing collection for 100% variable binding):**
- `layout/frame-width` = **393** · `layout/frame-height` = **852** (Base mobile frame: iPhone 15/16 Pro)
- `layout/safe-top` = **59** · `layout/safe-bottom` = **34** (Device safe areas)
- `layout/nav-clearance` = **104** (Bottom content padding to clear floating nav)
- `layout/touch-min` = **44** · `layout/touch-driver` = **56** (Minimum touch targets)
- `layout/icon-grid` = **24** (Icon grid size)
- `stroke/icon` = **1.75** · `stroke/route` = **5** · `stroke/route-casing` = **9** · `stroke/check` = **3** (Drawing weights for icons, the map route line and the check mark only. **Never used as an element border.**)
- `size/dot-xs` = **6** · `size/dot-sm` = **8** · `size/dot-md` = **10** · `size/dot-user` = **14**
- `size/checkbox` = **22** · `size/knob` = **24** · `size/switch-h` = **32** · `size/switch-w` = **52**
- `size/handle-w` = **36** · `size/avatar-md` = **40** · `size/avatar-lg` = **64** · `size/control-md` = **48** · `size/input-lg` = **52**
- `size/nav-height` = **64** · `size/quick-tile` = **72** · `size/stat-card-w` = **170** · `size/content-width` = **353**
- `size/zoom-pill-h` = **88** · `size/hero-map-h` = **548** · `size/welcome-sheet-h` = **332**
- `size/onboarding-sheet-h` = **304** · `size/progress-seg-w` = **88**
- `size/auth-hero-h` = **280** · `size/auth-hero-copy-w` = **280** · `size/auth-mascot-w` = **130** · `size/auth-mascot-h` = **176**
- `size/confirm-w` = **353** · `size/confirm-h` = **56** · `space/confirm-px` = **14** · `size/icon-xs` = **16** · `size/matrix-dot` = **2** · `size/matrix-gap` = **2** · `size/matrix-grid` = **14** (the two confirm radius tokens, `radius/confirm-idle` and `radius/confirm-circle`, live in the Radius collection, see 4.2)
- `size/bell-btn` = **36** · `size/weather-pill-h` = **36** (44 px hit area kept) · `size/weather-pill-w` = **112** · `size/weather-icon-lg` = **48** · `size/weather-icon-box` = **64** · `size/search-pill-h` = **46** · `size/home-content-w` = **361** (Home screen uses `space/4` 16 px horizontal margin and fluid `FILL` card width so it scales cleanly from 360 px to 430 px wide)
- `layout/home-top` = **71** (Home content top: `layout/safe-top` 59 + `space/3` 12) · `size/mascot-hero-h` = **160** · `size/mascot-hero-w` = **393** · `size/mascot-band-h` = **84** · `size/mascot-art-w` = **132** · `size/mascot-art-h` = **150** · `size/speech-bubble-w` = **233** · `size/speech-tail-w` = **14** · `size/speech-tail-h` = **16**
- `size/slider-track` = **4** (thin slider track) · `size/tab-underline` = **2** (underline tab indicator, a filled bar, not a border)
- `size/menu-w` = **264** (plus menu width) · `size/separator` = **1** (separator bar height) · `size/timeline-line` = **4** (stop timeline rail) · `size/stop-dot` = **12** · `size/stop-dot-end` = **20** (first / last stop marker, also the rail column width)

**Layout rules**
- Screen horizontal padding: **20** (`space/5`)
- Card inner padding: **16** (`space/4`, stat tiles) or **20** (`space/5`, feature cards)
- Gap between cards: **12** (`space/3`). Gap between sections: **24** (`space/6`).
- Bottom content padding: **104** (`layout/nav-clearance`, clears the floating nav)
- **No header or top bar.** Screens start at `layout/safe-top` with content (the plus-menu pages and the History inner pages use `PageHead`, see 6.4). On inner screens, back and close use a floating `iconbutton` (44 px, white, `shadow/soft`) at the top-left, `space/4` from the edge, just below `layout/safe-top`. It floats over content and is not a bar.
- **Auth hero** (`bg/auth-hero` → `primary/default` ink, Login / Sign Up only): flat fill, no gradient. Title `text/inverse`, subtitle `text/on-hero-subtle`; fixed height `size/auth-hero-h` (280), top padding `layout/safe-top` (59), copy top-aligned (16 px heading inset, title-to-subtitle gap `space/2` 8). Title and subtitle are capped at `size/auth-hero-copy-w` (280). `[APP LOGO]` may sit inside the auth hero, above the title.
- Auth mascot (`Login / Mascot`): `Reference/mascot2.jpg` (black background removed), `size/auth-mascot-w` × `size/auth-mascot-h` (130 × 176), peeking in from the right edge: 40 px (`space/10`) of its width is clipped by the screen frame, feet overlapping the sheet top by `space/2` (8). Layered above the sheet. One mascot per screen, never on cards or buttons.
- Auth form shape consistency: on auth sheets, the role segmented control track, and the primary submit button use `radius/md` (16) to match the text fields; selected/inactive segments use `radius/sm` (12). The auth role selector (`Control/RoleSelect`) uses a white `bg/default` indicator with `shadow/soft` and `text/primary` label, inset 8 px (`space/2`) inside a 56 px track, so the submit button stays the only black fill on the sheet. Icon-only social buttons stay circular and have no outline.
- Auth shell per role: Login ships as two frames, `Commuter Login` (Commuter) and `Driver Login`. Both are the same 393 × 852 vertical auto-layout shell — hero 280, form sheet, mascot — cloned rather than rebuilt. Only two things differ: which `Control/RoleSelect` variant is selected (Driver starts on `Role=Driver`) and the subtitle copy ("Sign in to see live jeepneys near you." vs "Sign in to go online and manage your trips."). Switching chips swaps the variant in place via the component's own 200 ms Smart Animate, and on the two real screens the chip is overridden at instance level to navigate to the other role's frame instead (Smart Animate 200 ms ease-out, resetting every field and checkbox on the new frame to empty, `Chip/Driver` on Commuter → `Driver Login`, `Chip/Commuter` on Driver → `Commuter Login`). The override lives on the instance, so the `Control/RoleSelect` component keeps its in-place `CHANGE_TO` behaviour for any context that has no second frame. Tapping the already-selected chip does nothing. Any further auth screen (Sign Up, OTP) should clone this shell.
- Always respect device safe areas (`layout/safe-top`=59, `layout/safe-bottom`=34).
- Home layout order, top to bottom: `Role/Commuter/GreetingRow` at `layout/home-top` (71) → `Role/Commuter/MascotHero` → cards. The greeting row carries the date overline + greeting on the left and the weather pill + notification bell on the right, flush left at `space/0`; it is page content, not a header bar, and there is **no calendar icon box**. Home has **no search bar and no saved-place chips** (`Home` / `School` / `Work`) — search lives on Map — so the first card sits `space/3` (12) under the hero. A full-width white `Top Band` (`bg/default`, no radius, no shadow) sits behind the greeting row and the top of the hero, from the top of the screen (y 0) down to the hero's charcoal band (y 199), so the top of Home reads as one white area that ends at the band; the cards below sit on `bg/app`.
- Home mascot hero (`Role/Commuter/MascotHero`): full-bleed `size/mascot-hero-w` 393 × `size/mascot-hero-h` 160 (`clipsContent: true`), edge to edge, its top part over the white `Top Band`, no radius and no shadow. A flat light-black band in `bg/mascot-band` `#262B35` (alias of `primary/pressed`) fills the lower `size/mascot-band-h` 84 px (y 76 to 160). Half-body waving mascot artwork (`Reference/mascotHome.png` cropped to tight bounds in `Reference/homepageMascot-cutout.png`, `size/mascot-art-w` 132 × `size/mascot-art-h` 150) sits at x `-4`, y `14`, flush with the band's bottom edge at y 160. Speech bubble: compact white `bg/default`, `radius/lg` 20, `size/speech-bubble-w` 233 × 90 at x 132, y 54, `space/3` 12 vertical / `space/4` 16 horizontal padding, `space/1` 4 gap, `shadow/raised` (so it stands out on the white `Top Band`), with a left-pointing `Bubble Tail` vector (`size/speech-tail-w` 14 × `size/speech-tail-h` 16 at x 120, y 78, 24 px below the bubble top so it stays clear of the rounded corner for 2- or 3-line messages, `bg/default`, `shadow/raised`, layered behind the bubble) pointing toward the mascot; label `LOC8` in `type/overline` `bg/mascot-band` (`#262B35`, matching the light-black band), 3-line message in `type/caption` `text/secondary` (`"Welcome, Ana! I'm Loc8. I'll help you track live jeepneys, free seats, and arrival times in one place."`). One mascot hero per screen, never inside a card.
- History mascot hero: History uses the same `Role/Commuter/MascotHero`, edge to edge, `space/5` (20) under the title row (`History` `h1` + filter `iconbutton`), so the hero starts at y 131; the trip groups follow `space/5` below it. The nested mascot is swapped (instance override) from `Mascot/Wave` to `Mascot/History`; the component itself and Home keep `Mascot/Wave`. Message: `"You took 8 rides this week, Ana! Tap a trip to rebook it or see the details."`. A white `Top Band` (`bg/default`, no radius, no shadow) runs from y 0 down to the hero's charcoal band (y 207), as on Home.

### 4.2 Radius

Radius is kept everywhere. Shapes are defined by radius + flat fill + shadow, never by a border.

| Token | px | Use |
|---|---|---|
| `radius/none` | 0 | Full-bleed surfaces (for example the mascot hero) |
| `radius/xs` | 7 | Checkbox, micro tags |
| `radius/sm` | 12 | Small chips, thumbnails |
| `radius/md` | 16 | Inputs, list rows, select menus |
| `radius/lg` | 20 | Stat tiles |
| `radius/xl` | 24 | Cards |
| `radius/2xl` | 28 | Bottom sheets (top corners) |
| `radius/pill` | 999 | Buttons, chips, nav, search, segmented control |
| `radius/confirm-idle` | 16 | `Button/Confirm` at rest (same value as `radius/md`) |
| `radius/confirm-circle` | 28 | `Button/Confirm` while collapsed to a circle (half of `size/confirm-h`) |

### 4.3 Elevation

These are Figma **effect styles**, not variables. Shadows replace borders for separating surfaces.

| Token | Value | Use |
|---|---|---|
| `shadow/card` | `0 2 12 rgba(0,0,0,0.06)` | Flat white cards, weather pill, search pill and notification bell button on `bg/app` (`#F9FAFC`) |
| `shadow/soft` | `0 4 16 rgba(15,17,21,0.06)` | White cards on white, floating iconbuttons |
| `shadow/raised` | `0 8 24 rgba(15,17,21,0.10)` | Sheets, menus, hero-overlap cards, mascot speech bubble, floating nav pill and its action button |
| `shadow/control` | `0 1 3 rgba(15,17,21,0.18)` | Small controls only: the unchecked checkbox box |

White cards use a shadow only. No hairline, no outline.

## 5. Iconography and imagery

- Icon style: **outline icons, 1.75 stroke, rounded caps and joins, 24 px** (Lucide-style). Active nav icons use the filled variant. (This is the icon drawing style, not an element border.)
- Icons in tinted circles: 44 px circle with pastel fill and its ink color for the icon.
- Key icons: home, map, start (play) / end (stop square), flame (hotspots), user-circle, bell, pin, cloud-sun (partly cloudy: `weather/sun` sun + `text/inverse` cloud, the one two-color icon), plus (opens the plus menu), message (chat), arrow-up (send), chevron-left (back), bus/jeepney, seat, shield (SOS), clock, cloud (weather), filter (History filter button), refresh (Rebook), flag (Report issue), pencil (Edit), globe (Language), help-circle (FAQ rows), file-text (Terms), log-out (Log out). The last 5 come from Lucide (lucide.dev, Lucide's `circle-help` is `Icon/help-circle`) and are redrawn at the 1.75 stroke.
- Hero visual: flat vector illustration, soft shadows, route-colored jeepney. Transparent PNG/SVG, placed top-right and slightly cropped by the screen edge. Its wheels overlap the first card's top edge by about 24 px.
- Loc8 mascot: a navy VR-helmet rider with an `8` keychain. Home uses `Reference/mascotHome.png` (tightly cropped in `Reference/homepageMascot-cutout.png`) in the `Role/Commuter/MascotHero` band; History uses the animated full-body `AssestRef/newMascot.gif` (`Mascot/History`) in the same band; auth screens and the History empty state use `Reference/mascot2.jpg`. Brand-color artwork — an intentional exception to the token palette, never recolored, never redrawn.
- Avatars: circle, 40 px (list) or 64 px (profile), no ring.
- No stock photos of people in core flows.

## 6. Components

All components define default, pressed, disabled, and (where relevant) loading states. Minimum touch target **44 x 44** (driver mode: **56**). No component has a border or outline in any state.

### 6.1 Buttons

| Component | Spec |
|---|---|
| **primarybutton** | Pill, height 56 (large) / 48 (medium) / 40 (small). Fill `primary/default`, text `text/inverse` at `body-lg` 600. Pressed `primary/pressed` and scale 0.98. Disabled `primary/disabled`. Loading: spinner replaces label, width stays. Full width in forms and sheets. |
| **secondarybutton** | Same sizes. Fill `bg/muted`, text `text/primary`, no border. **No outline variant.** Optional leading brand logo (`Has Logo` boolean + `Logo` INSTANCE_SWAP, hidden by default; logo 24 / 20 / 16 px for Large / Medium / Small). Social sign-in uses this with `Logo/Google` and `Logo/Facebook`. |
| **iconbutton** | 44 px circle, white fill, `shadow/soft`, icon 22 px. Notification badge: 8 px `error` dot, or count pill (min 18 px) at top-right. The Home notification bell is the one exception: it is `size/bell-btn` (36). |
| **floatingbutton** | 56 px circle, `accent/default`, white icon 26 px, `shadow/raised`. Used for the center nav action and map recenter (recenter is 44 px, white). Stop/End state uses `error` ink `#D93036`. |
| **cta-button** | Pill 56, fill `accent/default`, white text, optional trailing chevrons. For the single hero action (onboarding Next, empty-state action). Do not show next to a primarybutton on the same view. |
| **togglebutton** | Two forms. **Segmented**: track `bg/muted` pill, height 44, selected segment `primary/default` with white text, 200 ms slide. **Switch**: 52 x 32 track (`size/switch-w` × `size/switch-h`), 24 px white circle knob (`size/knob`) with 4 px (`space/1`) equal inset clearance on all sides (`32 - 2×4 = 24 px`), on `primary/default`, off `bg/strong`. |
| **confirmbutton** (`Button/Confirm`) | Interactive morphing button inside a full-width centered flex wrapper (`.confirm-wrap { display: flex; justify-content: center; align-items: center; width: 100%; }` — fixed/full section width, never shrink-to-fit, no `margin-left: 0`, `align-self: flex-start`, or `text-align: left`, so left and right edges collapse inward and expand outward symmetrically from the center). Button pill (`size/confirm-w` 353 × `size/confirm-h` 56, `radius/confirm-idle` 16 [`radius/md`], fill `primary/default` [`--stage-accent`], centered `"Verify"` label in `text/inverse` [`--stage-on-accent`] at `type/body-lg` [Plus Jakarta Sans 16 px / 24 px SemiBold], `shadow/soft`, horizontal padding `space/confirm-px` 14, `-webkit-font-smoothing: antialiased`, `text-rendering: optimizeLegibility`). Tapping sets `data-animating` (`will-change: transform, opacity, filter, width, border-radius` on button and children only while `[data-animating]` is present) and shrinks width symmetrically toward the center from measured `idleW` (`size/confirm-w` 353) → `size/confirm-h` × `size/confirm-h` (56 × 56 perfect circle, collapsed width derived from `--confirm-h`, never hardcoded) while animating `border-radius` from `radius/confirm-idle` (16 px) → `radius/confirm-circle` (28 px, `calc(var(--confirm-h) / 2)`) over **300 ms** `cubic-bezier(0.22, 1, 0.36, 1)` (`padding: 0`), fading out the centered `"Verify"` label (**250 ms** `ease-in-out`, `opacity: 0`, `filter: blur(2px)`, `transform: none` — no scale on hidden label so browser does not retain a low-res raster layer) into a 4×4 rounded dot-matrix orbit loader (`size/matrix-grid` 14 × 14, `size/matrix-dot` 2 px dots, `size/matrix-gap` 2 px gap; corners `[0, 3, 12, 15]` hidden, 8 perimeter dots `[1, 2, 7, 11, 14, 13, 8, 4]` pulsing clockwise from 35% to 100% `text/inverse` on a **1200 ms** `ease-in-out` cycle, center 4 dots at 35% `text/inverse`) for **2000 ms** (`aria-label="Verifying"`, `aria-busy="true"`), then swapping (**250 ms** `ease-in-out`, hidden icons use `opacity: 0`, `filter: blur(2px)`, `transform: scale(0.25)`; visible/resting state on label, loader, and check uses `opacity: 1`, `filter: none`, `transform: none` instead of `blur(0)` / `scale(1)`) to a 16 px check icon (`size/icon-xs` 16, `stroke/check` 3, rounded caps, `text/inverse`, `aria-label="Verified"`) for **1400 ms** before expanding symmetrically outward from the center back to measured `idleW` (`353px`) and `radius/confirm-idle` (`16px`) `Idle` (`aria-label="Verify"`) over **300 ms** `cubic-bezier(0.22, 1, 0.36, 1)`, then clearing inline `width`, `disabled`, and `data-animating` after `--resize-dur` (300 ms). Press state uses `primary/pressed` and scale `0.97` over **150 ms** `cubic-bezier(0.22, 1, 0.36, 1)` (held ≥150 ms on touch). Hover (mouse only): `brightness(1.15)`. Focus state: `primary/pressed` fill, no ring or outline. Reduced-motion (`prefers-reduced-motion: reduce`): removes all transitions and animations; state changes occur instantly. |

### 6.2 Navigation

| Component | Spec |
|---|---|
| **bottombar** | Floating glass pill: fill `bg/default` at 70% opacity with 16 px background blur, height 64, radius pill, 4 px inner padding, `shadow/raised`, 20 px (`space/5`) above the screen bottom (nav top at y 768 on the 852 frame). Icons 24 px. Inactive tabs are 44 × 56 with a `text/secondary` icon and no label. The active tab is an expanding black pill (`primary/default`, 56 px high, radius pill) with a filled `text/inverse` icon and label. The commuter bar has 4 items (Home, Map, History, Profile) in a 277 px pill, plus a separate round 64 px black action button (`primary/default`, `shadow/raised`) beside it, 12 px gap, 353 px total width. At rest it shows a white `Icon/plus` and opens the plus menu (`Menu/Plus`, see 6.4); the plus turns 45° into a close icon while the menu is open. While waiting it switches to `primary/pressed` with `Icon/pin` and the pulsing ping ring. Drivers use the same pill style with the Start/End Trip action button. Max 5 items. |
| **hamburgermenu / sidebar / collapsiblesidebar / megamenu / breadcrumbs / navbar / footer** | **Not used in the mobile app.** Reserved for the coop/LTFRB/LTO web dashboard and landing site. |

**There is no topbar, header or sticky navbar in the mobile app.** Do not add one. Page titles live inside the content (for example `type/h1` at the top of the scroll area). Back and close use the floating `iconbutton` described in 4.1.

### 6.3 Sections (mobile adaptations)

| Component | Spec |
|---|---|
| **authhero** | The only hero area in the app. Used on Login and Sign Up. Flat `bg/auth-hero` fill, `text/inverse` title, `text/on-hero-subtle` subtitle, mascot peeking from the right. See 4.1. |
| **onboardingsection** | Onboarding slides: 3 slides max, one illustration + title (`h1`) + one helper line each, flat background, page dots (active dot = 20 px pill `primary/default`, inactive 6 px circle `bg/strong`), Skip (secondarybutton small) and Next (cta-button). |
| **aboutsection** | App name, version, Terms and Privacy links as list rows. |
| **faqsection** | Collapsible rows: question `body-lg` 600, chevron rotates, answer `body` `text/secondary`. 16 px row padding, `space/2` gap between rows, no divider lines. |
| **contactsection** | Rows with tinted icon circles (message coop, report a problem, call). |

### 6.4 Cards and surfaces

| Component | Spec |
|---|---|
| **Card (white)** | `bg/default`, `radius/xl`, padding 16 to 20, `shadow/soft` (or `shadow/card` on `bg/app`). No border. |
| **Stat tile** | Tinted fill, `radius/lg`, padding 16. Label `caption` secondary, value `display` or `h1`, unit `body`. Optional 44 px icon circle top-right. |
| **List row** | Height 64, 44 px icon circle (tinted), title `body-lg` 600, subtitle `caption` secondary, trailing value or chevron. Rows are separated by `space/2` gap, not by lines. |
| **Bottom sheet** | White, top radius `radius/2xl`, 36 x 4 handle `bg/strong`, scrim `rgba(0,0,0,0.4)`, `shadow/raised`. |
| **Chip / badge** | Height 28, pill, `caption` 600, semantic or tint fill with matching ink. Optional 8 px leading dot. No border. |
| **Filter chip** (`Chip/Filter`) | Tappable pill, `layout/touch-min` 44 tall, `space/4` sides, `space/2` gap, `caption` label, no border. `Tone=Neutral` (single select): off `bg/muted` + `text/primary`, on `primary/default` + `text/inverse`. `Tone=R1`/`R2`/`R3` (multi select): off `bg/muted`, on a `Route Tint` layer in `route/n` at 16 % layer opacity + 16 px `Icon/check` and label in `text/primary`. Used in `Modal / History filter`. |
| **History filter sheet** (`Modal / History filter`) | Bottom sheet shell, `space/3` top / `space/5` sides / `layout/safe-bottom` bottom padding, `space/5` gap. Title row `Filter trips` `h3` + `Reset` `body` `accent/default` (44 hit area). `TIME PERIOD` and `ROUTE` groups: `type/overline` `text/secondary` label, then `Chip/Filter` rows (`space/2` gap, wrap). Full-width `Button/Primary` Large `Show 3 trips`. |
| **Rebook sheet** (`Modal / Rebook / R1`) | Same sheet shell. `Rebook this ride` `h3`; route tile (`bg/subtle`, `radius/lg`, 12 / 16 padding, `space/3` gap: 44 px `Route Square` as in `Card/Trip` + place `body-lg` / `Same route as today, 7:42 AM` `caption` `text/secondary`); 52 tall rows `Last fare` / `Last jeepney` (label `body` `text/secondary`, value `body-lg`) split by `Separator`; helper line `caption` `text/secondary`; `Button/Primary` Large `Find a jeepney on R1` over `Button/Secondary` Large `Cancel`. |
| **Trip details page** (`Commuter / 03 History / Trip details`) | `bg/app` page, no nav. `PageHead` (`Trip details` / `Today, 7:42 AM`). Content `space/5` sides, `space/6` gap: hero card (`bg/default`, `radius/xl`, `shadow/card`, `space/6` / `space/5` padding, centered, `space/2` gap: 56 px `Route Square`, place `h2`, fare `display`, `Chip/Semantic` Success `Completed`); `TRIP INFO` overline + card of 52 tall rows (Date, Time, Jeepney, Wait time, Fare) split by `Separator`. Footer (`space/3` top, `space/5` sides, `layout/safe-bottom` bottom, `space/3` gap): `Button/Secondary` Large `Report issue` with `Icon/flag` + `Button/Primary` Large `Rebook`, equal halves. |
| **Report issue page** (`Commuter / 03 History / Report issue`) | `bg/app` page, no nav. `PageHead` (`Report an issue` / `Tell us what went wrong`). Trip summary card (`Route Square` 44 + place `h3` / meta `caption` + fare `h3`); `WHAT WENT WRONG?` overline + card of `Input/Radio` rows split by `Separator`; `Input/Text` labelled `Details (optional)`; footer `Button/Primary` Large `Submit report`. |
| **Profile page** (`Commuter / 04 Profile`) | Reference: `AssestRef/Profile (full length)@1x.png`. `bg/app` page with `Nav/Commuter` (`Active=Profile`); the body scrolls under the fixed nav. Body padding `layout/home-top` top, `space/5` sides, `layout/nav-clearance` bottom, `space/6` gap. `Profile` `h1`. Profile card (`bg/default`, `radius/xl`, `shadow/card`, `space/5` padding, `space/4` gap): 64 px avatar (`size/avatar-lg`, `tint/lavender-fill`, initials `h2` `tint/lavender-ink`) with a 24 px `primary/default` edit badge (14 px `Icon/pencil` in `text/inverse`) at its bottom-right; name `h3`, email `caption` `text/secondary` (ellipsis), passenger type `Chip/Semantic` Info; `Button/Secondary` Small `Edit` with `Icon/pencil`. Then 3 groups, each a `type/overline` `text/secondary` label + `space/2` + a white card (`radius/xl`, `shadow/card`, `space/1` top and bottom padding) of rows split by `Separator` inset `space/4`: `PREFERENCES` (2 `ArrivalAlertRow` with `Control/Switch` On (Primary): Arrival alerts Peach `Icon/bell`, Live location Sky `Icon/pin`; `Row/List` Value `Language` / `English` Lavender `Icon/globe`), `HELP AND SUPPORT` (`Row/List` Chevron: discounts FAQ Lavender `Icon/help-circle`, seats and ETAs FAQ Sky `Icon/bus`, Report a problem Peach `Icon/flag`, Email cooperative Sky `Icon/mail`), `ABOUT` (Terms and Conditions Lavender `Icon/file-text`, Privacy Policy Lavender `Icon/shield`). Row titles wrap to 2 lines. Last: full-width `Button/Secondary` Large `Log out` with `Icon/log-out`, then the version line `caption` `text/secondary`, centered, `space/3` above it. Changes from the reference: no outlines on cards or buttons (fills and shadows instead), tinted icon circles instead of grey squares, Language shows the value without a chevron (`Row/List` Value has none), app name `Loc8`. |
| **Weather card** (`Role/Commuter/WeatherCard`) | Opens from the charcoal weather pill (Dynamic Island style): one element morphs from the pill (`size/weather-pill-w` 112 × `size/weather-pill-h` 36, `radius/pill`, flat `bg/mascot-band` fill, no stroke, `space/3` side padding, today's icon 16 (`Icon/cloud-sun`) on the left and `28°` in `type/mono-body` `text/inverse` on the right, pushed apart with space-between, `shadow/card`; focus fill `primary/default`) to a 361 wide card (`radius/xl`, `shadow/raised`) that overlays the content below. Open 350 ms, close 250 ms, `cubic-bezier(0.22, 1, 0.36, 1)`; the sky fades in over the white as it grows. Content, 20 px padding: place (`body-lg` 600), day name (`caption`, `weather/text-muted`, letter morph on change), temperature (`type/weather-temp`) with a 48 px weather icon in a 64 px box at the right, condition (`body` 600), `H: L:` line (`caption`, `weather/text-muted`). Below: 5 day tabs, track `weather/tab-track` `radius/md`, 4 px padding, tabs 48 tall `radius/sm` with a 16 px icon + `caption` label, sliding `weather/tab-pill`. Card fill is the same flat `bg/mascot-band` as the pill (no sky gradient). Weather icons are colored: sun and bolt in `weather/sun`, cloud in `text/inverse`. Today shows `Partly cloudy` with `Icon/cloud-sun`. Backdrop effects on the charcoal: drifting glow; rain and storm add falling streaks, storm adds a lightning flash. Sky cross-fade 700 ms; reduced motion hides rain and flash and stops all drifting. Prototype: `prototype/weather-island/index.html`. |
| **Plus menu** (`Menu/Plus`) | Grows out of the round nav button (64 px black circle) into a `size/menu-w` 264 wide white card (`bg/default`, `radius/xl`, `shadow/raised`, `space/2` padding) right-aligned with the nav, `space/3` above it. No grey scrim: the screen behind stays as it is, and `shadow/raised` alone lifts the card off it. Tapping anywhere outside the card closes it. Reference: `AssestRef/NewEvent.jpg`. Open 350 ms, close 250 ms, `cubic-bezier(0.22, 1, 0.36, 1)`; fill changes black → white as it grows, content fades in after 100 ms. Two rows (64 tall, `radius/md`, 12 px side padding, `space/3` gap, `space/1` between rows; focus/pressed fill `bg/subtle`) with a `Separator` between them (a `size/separator` 1 px `bg/muted` filled bar, not a stroke, inset `space/3` on both sides): `IconCircle/Tint` 44 px + title `body-lg` 600 + subtitle `caption` `text/secondary`. Row 1 `Chat` / `Ask Loc8 about jeepneys` with `Icon/message` on Lavender. Row 2 `Start waiting` / `Pick your stop and destination` with `Icon/pin` on Sky. Start waiting sits last so it is closest to the thumb. Tapping a row closes the menu and slides in that page, so the menu is closed when the commuter comes back. Close: the button (now ×), Esc, or tapping outside the card. Reduced motion: instant. Prototype: `prototype/destination-island/index.html` (behind Figma: no separator yet, and the old text sizes on the pages). |
| **Page title row** (`PageHead`) | Used only on full-screen inner pages: the plus-menu pages (Start waiting, Chat) and the History inner pages (Trip details, Report issue). Approved exception to the no-header rule. It stays fixed while the content below it scrolls, and has no fill of its own, no shadow and no divider. Padding `layout/safe-top` top, `space/5` sides, `space/3` bottom, `space/4` gap: 44 px back `iconbutton` (`Icon/chevron-left`, `bg/default`, `shadow/soft`, focus fill `bg/muted`), then title `h2` + subtitle `caption` `text/secondary`. |
| **Slide-in page** | Full 393 × 852 page (`bg/default`) that covers Home and the nav. Opens by sliding in from the right (`translateX(100%)` → 0, 350 ms `cubic-bezier(0.22, 1, 0.36, 1)`); back slides it out to the right, 250 ms, same curve. Esc or back closes it. Reduced motion: instant. |
| **Start waiting page** (`Page/StartWaiting`) | A slide-in page with a `PageHead`. Two steps on the same page. Title `h1` (`Where from?` in step 1, `Where to?` in step 2) + subtitle `body` `text/secondary` (`Pick the stop where you are waiting` → `Pick your destination` → `Check your fare`). In step 2 the From row sits under the title row (`space/5` sides, `space/3` bottom): a 44 tall button, `bg/subtle`, `radius/md`, 12 px side padding, `space/2` gap: 8 px route-color dot, `From` `caption` `text/secondary`, `Bugasong · Public Market` `caption` 600 (ellipsis), `Change` `caption` 600; tapping it goes back to step 1. Picking a From stop closes the route list for step 2. The route list fills the rest of the page and scrolls (`space/3` top, `space/5` side padding). Route rows (64 tall, `radius/md`, 12 px side padding, 12 px gap, `space/2` between rows, no dividers): 24 px halo (route color at 16 %) with a 12 px route-color dot, name `body-lg` 600, `R1 · 2 LIVE` in `mono-tag` `text/secondary`, `6 stops` `caption`, `Icon/chevron-down` that turns 180° when open. Closed row fill `bg/subtle`; open row fill = route color at 16 % and the halo turns `bg/default`. One route open at a time; the stop list opens with a 250 ms height animation. Stop timeline (44 px rows, `radius/md`): `size/timeline-line` rail in the route color (a filled bar, not a stroke) running dot to dot; ring markers made of two fills (route-color circle + `bg/default` core), `size/stop-dot` normally and `size/stop-dot-end` on the first and last stop, which are `body` 600 with a `First stop` / `Last stop` `caption`. Other stops `body`. A jeepney near a stop shows a 24 px chip (route color at 16 %, 6 px route dot, `J-014 · 3 MIN` in `mono-body`). From and To can be on different routes. Each picked stop: row fill route color at 16 %, filled marker core, name 600, and a 24 px `bg/default` pill tag `From` / `To` in `caption` 600 at the right; in step 2 the From stop cannot be tapped. Once To is picked a footer appears pinned at the bottom of the page (`bg/default` fill so the scrolling list ends cleanly at its top edge, 12 top / 20 side / `layout/safe-bottom` bottom, `space/2` gap, 250 ms height animation): `Bugasong · Public Market → San Jose · Market Stop` `caption`, a fare receipt tile (`bg/subtle`, `radius/lg`, padding 12 / 16, `space/1` row gap: a 44 tall `bg/muted` pill toggle `Regular` / `Student · Senior · PWD` whose selected segment is `bg/default` + `shadow/soft` with `text/primary` `caption` 600; then rows with a `caption` `text/secondary` label left and a `body` 600 value right: distance, base fare, extra km, discount (discount type only); last row `Estimated fare` with the value in `h3`), then a full-width `Button/Primary` Medium `Start waiting` (the only black fill on the page); it closes the page, shows a `Feedback/Toast` (`You are now waiting for J-014`), switches the nav button to the waiting state and opens `Role/Commuter/WaitingCard` on Home. Every time the page opens it is reset: no From or To, Regular fare type, route list closed and scrolled to the top. Reduced motion: every change is instant. Prototype: `prototype/destination-island/index.html`. |
| **Waiting card** (`Role/Commuter/WaitingCard`) | Home card shown only while the commuter is waiting, first card under `Role/Commuter/MascotHero`. 361 wide `FlatCard` surface, 16 px padding, `space/4` row gap. Rows: (1) `Role/Commuter/CardHeader` `Tone=Live`, title `Waiting for J-014`, meta `LIVE · 0S` in `type/mono-tag` `text/secondary`, arrow; the whole card is tappable and opens the waiting details. (2) ETA, a 48 px row: `type/display` number + `MIN` in `type/mono-tag`; under 1 minute it reads `Arriving` in `type/h3`. (3) Trip tile, 44 tall, `bg/subtle`, `radius/md`, 12 px side padding, `space/2` gap: 8 px dot in the From route color + `Bugasong · Public Market → San Jose · Market Stop` `type/caption` 600 (ellipsis). (4) Full-width `Button/Primary` Small `I boarded`, the only black fill in the card. Variants: `State=Hidden` (0 tall, invisible: the frame starts here, then grows into `Live` after 50 ms, 400 ms smooth-out), `State=Live`, `State=Arriving`, `State=Boarded` (label replaced by a `Icon/check` at `stroke/check`). Opens by growing from 0 to content height in 300 ms (`cubic-bezier(0.22, 1, 0.36, 1)`), content rises in after 100 ms, 40 ms apart; ETA digits roll like `Foundations/ETACountdown`, one ETA minute per tick; `I boarded` swaps to the check, holds 1000 ms, then the card closes (300 ms) and the nav button returns to the plus. Reduced motion: instant. Prototype: `prototype/waiting-card/index.html`, also wired in `prototype/destination-island/index.html`. |
| **Chat page** (`Page/Chat`) | A slide-in page. Reference: `AssestRef/Chat.jpg`. `PageHead` title `Chat`, subtitle `Ask about jeepneys, fares and stops.` Message log (scrolls, `space/5` sides, `space/4` between messages): Loc8 row = 40 px `Mascot/Head` + `Loc8` `body-lg` 600, `space/3` gap; Loc8 messages are plain `body` text with no bubble (greeting `Hi Ana!` with the name 600, then two short lines); the commuter's messages are right-aligned bubbles (`bg/muted`, `radius/lg`, padding 12 / 16, max 80 % wide, `body`). Composer pinned at the bottom (`space/5` sides, `layout/safe-bottom` bottom, `space/3` gap): `Input/Text` shell made taller (`bg/muted`, `radius/xl`, 16 padding, no border), 72 tall text area `body`, placeholder `text/tertiary`, 40 px round send button with `Icon/arrow-up` (`primary/default` + `text/inverse`; `primary/disabled` + `text/tertiary` while the input is empty), then the note `Loc8 can make mistakes. Check important details.` `caption` `text/secondary`, centered. |

### 6.5 Inputs

All inputs are borderless. State is shown by fill color. Input components have no error or invalid states: only empty and filled.

- Text field (`Input/Text`): 76 tall overall = label (`caption`, `text/secondary`) + `space/1` gap + 56 field. Field `radius/md`, fill `bg/muted`, 16 px side padding, 12 px gap, no border. No leading icon. Optional trailing 24 px icon (for example the password eye). No clear (×) button: tapping a filled field clears it. States: Default (empty, placeholder `text/tertiary`), Filled (value `body-lg` `text/primary`; passwords show as dots with `Icon/eye-off`) and Shown (password as plain text with `Icon/eye`).
- Select (`Input/Select`, pick-only combobox): same label + 56 field, value + trailing chevron-down. Open: field fill `accent/tint`, chevron rotates 180°, menu 8 px below the field (`bg/default`, `radius/md`, `shadow/raised`, `space/2` padding, `space/1` row gap). Rows 48 tall, `radius/sm`, `body-lg`; the selected row has an `accent/tint` fill and a check icon.
- Search: pill, height `size/search-pill-h` (46), leading search icon, fill white with `shadow/card` or `shadow/soft`, no border. Map only — Home has no search bar (see 4.1).
- OTP: 4 boxes, 48 x 56, `radius/md`, fill `bg/muted`, no border, no cursor inside the box. States: Empty and Filled (all 4 digits). Resend countdown in `caption` secondary.
- Date field (`Input/Date`): same shell as the text field with a leading calendar icon and a trailing chevron-down. On mobile it opens the date picker sheet.
- Date picker sheet (`Sheet/DatePicker`, date only): bottom sheet shell (see 6.4), title `h3`, month row (`body-lg`, 44 px prev/next hit areas), weekday row (`caption` `text/tertiary`), 7-column day grid with 44 px rows (`body-lg`), selected day = 40 px `primary/default` circle with `text/inverse` number, then a full-width `Button/Primary` "Done".
- Radio (`Input/Radio`): full-width 52 tall row, label `body` `text/primary` left, 22 px (`size/checkbox`) round radio right, `space/3` gap. Off = `bg/muted` fill + `shadow/control`; On = `primary/default` fill with an 8 px (`size/dot-sm`) `text/inverse` center dot. No ring or border.
- Checkbox (`Input/Checkbox`): 22 px, `radius/xs` (7), unchecked = `bg/muted` fill + `shadow/control` so the empty box stays visible, checked = `primary/default` fill with a `text/inverse` tick (`stroke/check`, round caps). Label `body` `text/primary`, `space/3` gap.

### 6.6 Feedback

- Toast (`Feedback/Toast`, `Type=Default` / `Alert`): pill at top (`layout/safe-top` from the top, centered), `primary/default` fill, `text/inverse` text with a leading status dot, 20 px side / 8 px vertical padding, 3 s.  Toast exit (every type), modeled on `Button/Confirm`: the instance keeps its size and only the inner pill moves. After 3 s the pill shrinks toward its center into a 44 px `primary/default` circle while the label and dot fade out with a 2 px blur (300 ms `cubic-bezier(0.22, 1, 0.36, 1)`), then an icon pops in, centered in a 24 px (`space/6`) round mask (10 px ring), from 25 % size, opacity 0 and blur 2 (250 ms ease-in-out): a 16 px (`size/icon-xs`) `Icon/check` in `text/inverse` on `Default`, `Waiting started` and `Boarded`, and the `Mascot/Head` on `Alert` (a check would read as success); it holds 1 s, then the circle fades out (200 ms ease-out). In the HTML prototype it fades and rises 8 px in 200 ms ease-out.
- Banner: full-width card with semantic fill and ink, icon left, one line, optional action.
- Empty state: 160 px illustration + one `h3` line + one cta-button.
- Skeleton: `bg/muted` blocks with soft shimmer (a flat color pulse, not a gradient sweep; use an opacity pulse of 1 to 0.6).

## 7. Motion

- Standard UI (buttons, chips, toggles): 200 ms ease-out. Sheets: 320 ms spring (damping about 0.85).
- Press: scale 0.98 and light haptic on primary actions.
- Marker movement: interpolate between GPS fixes over about 1 s, linear.
- Bottom nav: the nav stays in place when switching pages, and the black active tab slides to the tapped tab (Smart Animate, 300 ms, into the target page's fade-up entrance, see Page switch). Every commuter screen has its own top-level `Floating Commuter Nav` instance so the slide works.

### Form controls
Values come from the transitions.dev motion recipes. "Smooth-out" = `cubic-bezier(0.22, 1, 0.36, 1)`.

| Control | Motion |
|---|---|
| Text field fill (empty → filled) | Placeholder out and value in, 4 px rise + 2 px blur, 150 ms ease-in-out |
| Password show / hide | Dots ↔ plain text and eye-off ↔ eye icon swap, 250 ms ease-in-out |
| Text field clear (tap a filled field → empty) | Value out and placeholder back, 400 ms smooth-out |
| OTP entry | One tap fills all 4 digits, 150 ms ease-in-out. Tapping a full code clears it, 400 ms smooth-out |
| Select open / close | Menu from scale 0.97 + opacity 0, 250 ms; close 150 ms; both smooth-out. Chevron rotates with the open |
| Date picker sheet | Opens with the standard sheet motion (320 ms, from the bottom). Selection circle slides to the tapped day, 250 ms smooth-out |
| Checkbox | Box fill 150 ms, then tick draws in left to right 350 ms; uncheck 150 ms; all smooth-out |

### Page switch: staggered cascade
When the user switches pages, the new page builds in piece by piece, top to bottom.
- Old page: exits almost instantly, opacity 1 to 0 in 80 ms, no slide or scale.
- New page: the first content group appears first, with no delay.
- Then the content enters in order, one group at a time, each with a 100 ms delay after the previous group:
  1. Search or filter row
  2. Chips or segmented controls
  3. First card
  4. Remaining cards, 60 ms apart (cap the stagger at 5 items, the rest appear together)
- Each group: opacity 0 to 1 and translateY +12 px to 0, 250 ms, cubic-bezier(0.25, 0.8, 0.25, 1).
- Total time from tap to fully settled: 700 ms at most.
- Fixed elements (bottom nav, map base) never animate.
- Cards below the fold appear without animation.
- No bounce or overshoot.
- Reduce-motion: all groups fade in together over 150 ms, no translate, no stagger.
- **Figma build (fade-up, every commuter nav page):** used on the 4 main pages and on the Waiting and Boarded sets (`Home`, `Map`, `History`, `Account` - `Waiting` / - `Boarded`; Account uses the Profile groups of its own layout: step 1 title and subtitle, step 2 the first two cards). Not used as the entrance of `Home - Waiting Without Card`, `Home - Boarded With Toast` and `Home - Waiting / Boarded`, which keep their own motion; the nav tabs on `Home - Boarded With Toast` do go to the fade-up of the Boarded pages. Figma cannot overlap delays, so the cascade runs as steps through hidden copies of each page (`<page> / Enter 1`, `<page> / Enter 2`). `Enter 1` has every animated group 12 px lower at opacity 0; `Enter 2` has the step 1 group in place and the step 2 group still 12 px lower at opacity 0 (offsets use absolute position in these copies only). Every nav tab goes to the target page's `Enter 1` (Smart Animate 300 ms), then `Enter 1` → `Enter 2` → the page each run after 1 ms (Smart Animate 200 ms), all with cubic-bezier(0.25, 0.8, 0.25, 1). Total about 700 ms. Groups per page:
  - Home: step 1 greeting row, weather pill, mascot hero; step 2 waiting card (when shown), nearest jeepney card, fare card (unless it starts below the fold, as on `Home - Waiting`).
  - History: step 1 title row, mascot hero; step 2 the Today, Yesterday and Nov 8 groups (Nov 6 is below the fold and stays still).
  - Profile: step 1 title, profile card; step 2 Preferences and Help and support (About and Log out are below the fold and stay still).
  - Map: one step only, because the map base never animates. `Commuter / 02 Map / Enter 1` has only the card track 12 px lower at opacity 0, then goes to the page after 1 ms (Smart Animate 250 ms). Total about 550 ms. In this hidden copy the `Card/JeepneyCarousel` is detached, because a layer inside an instance cannot be moved. If the carousel changes, rebuild this copy from the Map page.
  - Top band, bottom blur strip, map base and nav are the same in every step, so they stay still.

## 8. Accessibility

- Contrast: body text at least 4.5:1, large text and icons at least 3:1. Do not use `text/tertiary` for essential info.
- Touch targets at least 44 px (driver mode 56 px).
- Never use color alone: pair every status color with an icon or label.
- Since there are no borders, focus, selected and error states must be clear through fill change, icon, or text, never through an outline.
- Support dynamic type, screen readers (labels on all iconbuttons), and one-hand reach (primary actions in the lower half).
- Moving-vehicle safety: no typing, no scrolling lists, and no multi-step flows while the driver is moving.

## 9. Do and don't

**Do**
- Keep white space generous; one idea per card.
- Use big numbers with small units.
- Use pastel tints to group by meaning (Sky = time, Mint = money, Lime = ready, Peach = alerts).
- Keep the bottom nav to 5 items, with one round action button at most.
- Separate surfaces with fill, radius, shadow and spacing.

**Don't**
- Don't use borders, strokes or outlines on any UI element, in any state. Map drawings are the only exception (see 2.6).
- Don't add a header, top bar or sticky navbar.
- Don't add gradients the user did not ask for (fills, hero, map, buttons, cards, scrims, fades). Only the components listed in 2.7 have one.
- Don't add routes beyond Bugasong, San Jose and Patnongon.
- Don't use more than one filled black button per view.
- Don't stack more than 4 cards before the user scrolls.
- Don't use shadows heavier than `shadow/raised`.
- Don't mix icon styles or add a new font.
- Don't show raw GPS jargon, exact commuter locations, or individual commuter identities (aggregate counts only).

## 10. Figma setup (for the foundations)

**Pages in Figma file:**
1. **Foundations**: Holds the Foundation Spec Board and all reusable UI components for future development.
2. **Login-Signup-OTP-Terms-Privacy**: Authentication and legal screens.
3. **Commuter**: Commuter role screens.
4. **Driver**: Driver role screens.
5. **Admin**: Coop/LTFRB/LTO web dashboard screens.

**Theme Mode:** Light mode only (`Light` mode in every variable collection).
**Base Mobile Frame:** `393 x 852` (with `59 px` top safe area, `34 px` bottom safe area, `20 px` side padding, `104 px` bottom nav clearance).

**Variable collections (3), all `Light` mode only:**
1. **Color**: groups `bg`, `text`, `primary`, `accent`, `tint`, `semantic`, `status`, `demand`, `route` (3 variables only), `map`. There is no `border` group. `bg/auth-hero` aliases `primary/default` and `bg/mascot-band` aliases `primary/pressed`.
2. **Spacing**: numeric variables `space/0` to `space/20`, plus `space/confirm-px`, `layout/*`, `stroke/*` (icon, route, route-casing, check only) and `size/*` tokens, so no value is hard-coded.
3. **Radius**: numeric variables `radius/none` (0), `radius/xs` to `radius/pill`, `radius/confirm-idle` and `radius/confirm-circle`.

**Styles (not variables):**
- **Text styles**: `type/display`, `type/h1`, `type/h2`, `type/h3`, `type/body-lg`, `type/body`, `type/caption`, `type/overline`, `type/greeting`, `type/mono-tag`, `type/mono-body` (see section 3).
- **Color styles (Paint)**: only the gradients in 2.7: `weather/sky-clear`, `weather/sky-cloudy`, `weather/sky-rain`, `weather/sky-storm`. No other paint styles exist.
- **Effect styles**: `shadow/soft`, `shadow/raised`, `shadow/card`, `shadow/control`.

In Figma, no layer may have a stroke used as a border. Delete any existing border strokes on components and replace them with the fill or shadow described above.

Keep these in sync with this file. If a token or style exists in only one place, fix the mismatch (Figma follows this file by default).

Component naming: `Button/Primary/Large/Default`, `Chip/Success`, `Card/Stat/Sky`, `Nav/Bottom/Active-Home`. Use auto layout everywhere and variants for states.

## 11. Component and asset registry (reuse these)

| Need | Use this | Where |
|---|---|---|
| Route label | `Badge/Route` (3 routes only: `R1 · Bugasong`, `R2 · San Jose`, `R3 · Patnongon`) | Foundations |
| GPS status | `Chip/GPS` | Foundations |
| Tinted icon | `IconCircle/Tint` | Foundations |
| Bottom nav (commuter) | `Nav/Commuter` (`Active=Home`, `Active=Map`, `Active=History`, `Active=Profile`; 353 × 64: glass pill 277 × 64 (`bg/default` at 70% + 16 px background blur) with `shadow/raised`, plus the separate 64 px black `Button/Waiting` (`State=Idle` with `Icon/plus`, `State=Waiting` and `State=Waiting Pulse` with `Icon/pin`) with `shadow/raised`, 12 px gap. The button sits inside a `Menu/Plus` instance named `Plus Menu`. Instances sit at y 768 on every commuter screen) | Foundations — Components / 04, Section: Nav/Commuter (Floating White Nav) & Button/Waiting |
| Plus menu | `Menu/Plus` (`State=Collapsed` 64 × 64 nav button, `State=Open` with an invisible full-screen tap area (`Scrim`, opacity 0) + 264 × 153 card; rows `Row / Chat`, `Separator`, `Row / Start waiting` using `IconCircle/Tint`, `Icon/message`, `Icon/pin`. Prototype: tap + to morph open (Smart Animate 350 ms), × or outside the card to close (250 ms). Row taps first change the menu back to `State=Collapsed`, then slide in `Commuter / 07 Chat` / `Commuter / 06 Start waiting`; these are set as instance overrides on each commuter screen, because a component on Foundations cannot link to frames on another page) | Foundations — Components / 07 Plus Menu, Pages & Chat. Inside `Nav/Commuter` |
| Separator | `Separator` (1 px tall filled bar, `size/separator` + `bg/muted`, stretches to its container) | Foundations — Components / 07 Plus Menu, Pages & Chat |
| Page title row | `PageHead` (props `Title`, `Subtitle`; back = `Button/Icon` Elevated with `Icon/chevron-left`) | Foundations — Components / 07 Plus Menu, Pages & Chat |
| Start waiting page | `Page/StartWaiting` (`State=Step 1`, `Step 1 R1 open` / `R2 open` / `R3 open`, `Step 2`, `Step 2 R1 open` / `R2 open` / `R3 open`, `Selected Regular`, `Selected Discount`; 393 × 852, `PageHead` + route list + fare footer. Prototype: tap route rows and stops to move between states. Stop names and jeepneys are placeholders) | Foundations — Components / 07 Plus Menu, Pages & Chat. On the Commuter page the flow runs as 10 frames: `Commuter / 06 Start waiting` (Step 1) and `Commuter / 06 Start waiting / <state>` for the other 9 states, each holding one instance locked to its state. Each tap is an instance override that navigates to the matching frame with the same Smart Animate timing, because a component on Foundations cannot link to Commuter frames. Back goes to `Commuter / 01 Home` (slide out right, 250 ms) and `Start waiting` goes to `Home - Waiting For Toast Only` |
| Waiting card | `Role/Commuter/WaitingCard` (`State=Hidden`, `Live`, `Arriving`, `Boarded`; 361 × 232, see 6.4; `Hidden` → `Live` runs by itself (timer) and `Live` → `Boarded` on tapping `I boarded`; built from `CardHeader`, `Foundations/ETACountdown` (static `Hold=Value` / `Hold=Arriving`), and `Button/Primary` Small. The ETA does not count down in Figma) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`). Instances on `Commuter / 01 Home / Waiting` (starts `Hidden`) and `Commuter / 01 Home / Waiting / Boarded`. Prototype flow: `Commuter / 06 Start waiting / Selected Regular` or `/ Selected Discount` (Start waiting button, page slides out to the right) → `Home - Waiting For Toast Only`, where the card grows in while the toast overlay moves in from the top and the card stays → tap `I boarded` → `Commuter / 01 Home / Waiting / Boarded` (1 s) → `Commuter / 01 Home` |
| Toast | `Feedback/Toast` (`Type=Default`, `Alert`, `Waiting started`, `Boarded` × `Motion=Static` (no motion), `Pill` → `Shrink` → `Circle` → `Faded` (every type runs the same exit on its own timers). The motion variants keep a fixed root as wide as that toast (no fill) around an inner `Toast Pill`; the pill holds `Status Dot`, `Toast Message` and a 24 px round clip: `Check Mask` with a 16 px `Icon/check` (`text/inverse`) on `Default`, `Waiting started` and `Boarded`, `Head Mask` with a `Mascot/Head` instance cropped to the head on `Alert`; see 6.6). Timers run only on instances: play it from the `Toast demo` flow on Foundations (frame `Toast demo` with one of each type, press R to replay). Not yet placed in a screen | Foundations — Components / 03 Inputs & Feedback, Section: Feedback/Toast & Feedback/Banner |
| Chat page | `Commuter / 07 Chat` frame (393 × 852, `PageHead` + message log + composer) | Page Commuter |
| Profile page | `Commuter / 04 Profile` frame (393 × 852, scrolling body + `Nav/Commuter`; see 6.4). Icons `Icon/pencil`, `Icon/globe`, `Icon/help-circle`, `Icon/file-text`, `Icon/log-out` | Page Commuter. The 5 icons are on Foundations, row `Icons (new)` |
| Mascot head avatar | `Mascot/Head` (`Reference/mascot-head.png`, head cropped from `Reference/mascot_transparent.png`, 40 × 40, brand-color artwork, never recolored) | Foundations — Components / 07 Plus Menu, Pages & Chat |
| Buttons | `Button/Primary/{Large,Medium,Small}/{Default,Pressed,Disabled}` | Foundations |
| Jeepney transit card | `Card/Jeepney` (`Route=R1`…`Route=R3`; 320 × 164, occupancy-first — see anatomy below) | Foundations (Components / 04) |
| Interactive swipe deck | `Card/JeepneyCarousel` (`Active=1`…`Active=3`; each variant is 393 × 852 — a 2× `Map/Base` viewport panned to that route's jeepney plus the card track at `y = 530`, so the card bottom sits at `748`, `space/5` (20) above the nav top at `768`. The component has no nav of its own; each map screen uses its own `Nav/Commuter` instance. No pagination dots, drag handle or slider cue — the deck is read from the cards themselves and the jeepney markers; drag left = next, drag right = previous, clamped at the ends; tapping a card or a jeepney marker switches state. `See more` on the active card of every `Sheet=Closed` variant opens the sheet-only modal frame `Modal / Jeepney details / R1`…`R3` (393 × 414, a clipped `Sheet=Open` instance) as an overlay at bottom center with a `rgba(0,0,0,0.1)` dim background, Move in from bottom with Smart Animate (Gentle), so it covers the bottom nav; Close or tapping outside closes it. The link lives in the component, not as an instance override, because instance overrides are lost when a swipe changes the variant) | Commuter page — component set at x 5000 (moved from Foundations so its variants can link to the Commuter modal frames; must stay in one horizontal row for drag direction). The demo instance on Foundations cannot open the modals |
| Full-screen label-free base map | `Map/Base` (393 × 852, edge to edge, flat fills, no labels, one road, 3 live jeepney markers bound to `route/1`…`route/3`) | Foundations — Components / 05 Map |
| Social brand logos | `Logo/Google`, `Logo/Facebook`, `Logo/Apple` (24 px, fixed brand colors — intentional exception, not token-bound) | Foundations — Section: Logo/* (in Components / 01 Primitives & Status) |
| App mascot | `Login / Mascot` image frame (`Reference/mascot2.jpg` with the black background removed, FIT; 130 × 176 on auth screens, 160 × 160 on the Commuter History empty state; brand-color artwork, intentional exception, not token-bound). Home uses the same character waving in `Role/Commuter/MascotHero`, from `Reference/mascotHome.png` (`Reference/homepageMascot-cutout.png`) | Login screens `Commuter Login`, `Driver Login`, `Create Account` (page Login-Signup-OTP-Terms-Privacy), `Commuter / 03 History / Empty` and `Commuter / 01 Home` (page Commuter) |
| Auth role selector | `Control/RoleSelect` (`Role=Commuter` / `Role=Driver`; 353 × 56 (`space/14`) track `bg/muted` `radius/md`, chips keep a 48 px hit area; sliding `Indicator` `bg/default` + `shadow/soft`, `radius/sm`, inset 8 px (`space/2`); active ink `text/primary`, inactive `text/secondary`). Prototype: tapping the inactive chip changes to the other variant, Smart Animate 200 ms ease-out | Foundations — Components / 02, section after Control/Segmented. Instances on `Commuter Login` (Commuter) and `Driver Login`, each overriding the inactive chip to navigate to the other frame instead of swapping in place |
| History trip row | `Card/Trip` (`Route=R1` / `R2` / `R3`; props `Place`, `Meta`, `Fare` (TEXT). 353 wide, `bg/default`, `radius/xl`, `shadow/card`, **no border**, clips content. `Details` row: 16 px padding, `space/3` gap: 44 px `Route Square` (`radius/sm`, a `Route Tint` layer in `route/n` at 16 % layer opacity, code in `type/overline` `text/primary`) + place `type/h3` over meta `type/caption` `text/secondary` (`7:42 AM · J-014 · 4 min wait`) + fare `type/h3` + 16 px `Icon/chevron-right` `text/tertiary`; the whole row opens trip details. Then a full-width `Separator`, then a 44 tall `Actions` row split in two equal halves by a 1 px `bg/muted` bar: 16 px `Icon/refresh` + `Rebook` `type/body` `accent/default` | 16 px `Icon/flag` + `Report issue` `type/body` `text/secondary`) | Foundations — Commuter Components Row 2, instances on the `Commuter / 03 History` frames |
| Filter chip | `Chip/Filter` (`Tone=Neutral`, `R1`, `R2`, `R3` × `Selected=Off` / `On`; prop `Label` (TEXT); see 6.4) | Foundations — Components / 03, Section: Chip/Filter & Input/Radio |
| Radio row | `Input/Radio` (`Selected=Off` / `On`; prop `Label` (TEXT); see 6.5) | Foundations — Components / 03, Section: Chip/Filter & Input/Radio |
| History inner pages and sheets | `Modal / History filter`, `Modal / Rebook / R1` (393 wide, sheet only), `Commuter / 03 History / Trip details`, `Commuter / 03 History / Report issue` (393 × 852); see 6.4. One set per trip card: the frames above are for the first card (Today, R1), and each other card has its own `Modal / Rebook / <route> (<day>)`, `Commuter / 03 History / Trip details / <day> <route>` and `.../Report issue / <day> <route>` (Yesterday R2, Nov 8 R3, Nov 6 R2). Prototype, the same on all 3 History screens: tap a card → its Trip details (Move in from the left, 300 ms ease-out); `Rebook` → its rebook sheet as an overlay (Move in, 300 ms); `Report issue` → its Report issue page; the filter button → `Modal / History filter` overlay. Back on Trip details and Report issue uses the Back action, so it returns to the History screen that opened it | Page Commuter: first set in row y 2577, the other 3 sets in rows y 7029, 7981 and 8933 (x 1030 / 1503 / 2000) |
| Morphing confirm button | `Button/Confirm` (`State=Idle`, `State=Pressed`, `State=Loading 1`…`State=Loading 8`, `State=Done`; 353 × 56 `radius/confirm-idle` 16 `primary/default` + `text/inverse` + `shadow/soft` shrinking to 56 × 56 circle (`radius/confirm-circle` 28) with 14 × 14 4×4 orbit dot loader and 16 px stroke-3 `Icon/check`, then returning to 353 × 56; label TEXT property, default `Verify`) | Foundations — Components / 02 Buttons & Controls. Instance `Button / Verify` on `Verify Account` (`OTP / Actions` slot, replaces the old `Button/Primary/Large`) |
| OTP code input | `Input/OTP` (`State=Empty`, `Filled`; 4 boxes 48 × 56 + resend caption. Prototype: one tap fills the whole code `4829`, tap again to clear) | Foundations — Section: Input/OTP (Interactive). Instance on `Verify Account` |
| Text field | `Input/Text` (`State=Default` (empty), `State=Filled`, `State=Shown` (password visible); props `Label`, `Placeholder`, `Value`, `Shown value` (TEXT), `Leading icon` (BOOLEAN, off) / `Trailing icon` (BOOLEAN + INSTANCE_SWAP). No clear button. Prototype: tap an empty field to fill it, tap a filled field to clear it, tap the eye to show / hide the password) | Foundations — Components / 03, Section: Input/Text (Interactive). Instances on `Commuter Login`, `Driver Login` and `Create Account` |
| Select (pick-only combobox) | `Input/Select` (`State=Closed` / `Open` × `Value=None`, `Option 1`…`Option 3`, plus `State=Disabled`; props `Label`, `Placeholder`, `Option 1`…`Option 3` (TEXT), `Show label` (BOOLEAN). Prototype: tap to open, tap a row to pick) | Foundations — Components / 03, Section: Input/Select & Input/Checkbox. Not placed on a screen yet |
| Date field | `Input/Date` (`State=Empty`, `Focus`, `Filled`; props `Label`, `Placeholder`, `Value`) | Foundations — Components / 03, Section: Input/Date & Sheet/DatePicker. Instance on `Create Account`: one tap fills the field and opens `Overlay / Birth date picker` |
| Date picker sheet | `Sheet/DatePicker` (`Day=1`…`Day=31`; props `Title`, `Month`. Tapping a day changes to that day's variant; Done closes the overlay) | Foundations — Components / 03, Section: Input/Date & Sheet/DatePicker. Used in the `Overlay / Birth date picker` frame (page Login-Signup-OTP-Terms-Privacy) |
| Checkbox | `Input/Checkbox` (`State=Unchecked`, `Filling` (motion-only), `Checked`; prop `Label`. Prototype: tap to check / uncheck) | Foundations — Components / 03, Section: Input/Select & Input/Checkbox. "Remember me" on the Login screens |
| Commuter Home greeting row | `Role/Commuter/GreetingRow` (361 × 40, no icon box: stacked `Date#946:0` `"TODAY, 11 NOVEMBER"` in `type/mono-tag` and `Greeting#946:1` `"Good morning, Ana"` in `type/greeting` left, starting flush at x 0; 112 × 36 flat charcoal `Weather Pill` (`bg/mascot-band`, no stroke, `Icon/cloud-sun` left and `text/inverse` `28°` in `type/mono-body` right) and 36 × 36 circular `Button/NotificationBell` with `Icon/bell` + unread dot right; all surfaces use `shadow/card`, **no border**) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instance on `Commuter / 01 Home` |
| Home mascot hero | `Role/Commuter/MascotHero` (393 × 160 full-bleed, `clipsContent: true`; flat light-black `bg/mascot-band` `#262B35` band 393 × 84 at y 76, no radius, no shadow; half-body waving mascot artwork 132 × 150 at x -4, y 14 flush with the band bottom; compact white `radius/lg` 20 speech bubble 233 × 90 at x 132, y 54 with left-pointing `Bubble Tail` 14 × 16 at x 120, y 78 (behind the bubble, `shadow/raised`), `space/3` 12 vertical / `space/4` 16 horizontal padding, `space/1` 4 gap, `shadow/raised`, label `LOC8` in `type/overline` `bg/mascot-band` + 3-line message `type/caption` `text/secondary`; `Message#964:0` TEXT property) | Foundations — Commuter Components Row 4, instance `Mascot Hero` on `Commuter / 01 Home` and on the 3 History screens (`Commuter / 03 History`, `History - Waiting`, `History - Boarded`) |
| Waving mascot | `Mascot/Wave` (132 × 148, animated GIF fill; GIF plays continuously in Figma Presentation/Prototype view; static resting pose in editor mode) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`). Used in `Role/Commuter/MascotHero` on Home |
| History mascot | `Mascot/History` (132 × 148, animated GIF fill `AssestRef/newMascot.gif` (converted from `newMascot.webp`, 55 frames, looping), scale FIT; brand-color artwork, never recolored) | Foundations — Section: Commuter Role Components, right below `Mascot/Wave`. Swapped into the `Mascot Hero` instances on `Commuter / 03 History`, `History - Waiting` and `History - Boarded` |
| Flat card header row | `Role/Commuter/CardHeader` (`Tone=Live` green `status/live` dot / `Tone=Explore` blue `accent/default` dot + `Title#946:2` in `type/caption` `text/secondary` left; `Meta#946:5` in `type/mono-tag` `text/tertiary` + 16 px `Icon/arrow-right` right, with `Show Meta#946:8` and `Show Arrow#946:11` booleans). This is a card title row, not a page header. | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instances across `Commuter / 01 Home` cards |
| Flat white card surface | `Role/Commuter/FlatCard` (`bg/default` `#FFFFFF`, `radius/xl` 24, `space/4` 16 px inner padding, **no border/stroke**, `shadow/card` `0 2px 12px rgba(0,0,0,0.06)`) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), used across `Commuter / 01 Home` on `bg/app` (`#F9FAFC`) |
| Nearest jeepney card | `Role/Commuter/NearestJeepney` (`State=Live` 361 × 320 across `Route=R1` / `R2` / `R3` and `Alert on=Off` / `On`, `State=Arriving` 361 × 298, `State=Full` 361 × 320, `State=No jeepneys` 361 × 188, `State=Loading` 361 × 320, plus `State=Pressed Track` and `State=Pressed Alert` 361 × 320; props `ETA#1000:6`, `Sub line#1000:12`, `Seats free#1000:18`, `Updated#1000:24` (TEXT), `Route`, `Alert on`, `State` (VARIANT); HTML prototype not yet in the repo; anatomy and motion below) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instance `Card/NearestJeepney` on `Commuter / 01 Home` |
| Fare card | `Role/Commuter/FareCard` (361 wide `FlatCard` surface, 16 px padding, `space/4` section gap. Header: `Fares` `type/caption` `text/secondary` + compact `From` select trigger (a small size variant of `Input/Select`: `bg/muted` pill `size/bell-btn` 36 tall inside a 44 hit area, `From` `type/caption` `text/secondary` + town `type/caption` 600 + 16 px `Icon/chevron-down` that turns 180° when open; pill turns `accent/tint` when open or focused; menu and its motion follow the `Input/Select` spec, each row with an 8 px route-color dot). Big value `type/display` + `40 km to San Jose` `type/body` `text/secondary`. Underline tabs `Regular` / `Student · Senior · PWD`: text buttons `type/body` 600, 44 tall, `space/5` gap, active `text/primary`, inactive `text/secondary`; under the active label a `size/tab-underline` 2 px `primary/default` filled bar (`radius/pill`) that slides and resizes in 200 ms ease-out; no baseline rule under the tabs. Destination bar sliders (one row per other municipality, `space/2` gap, 44 tall): town name button `type/caption` 600 (tap to select it and reset to the whole trip); the bar is a slider from 1 km to that town's distance, starting full: thin `size/slider-track` 4 `bg/strong` pill track with a flat fill in that town's route color (`route/1` Bugasong, `route/2` San Jose, `route/3` Patnongon) ending at the knob centre, `size/knob` 24 knob filled with the same route color, `shadow/raised` (turns `primary/default` on keyboard focus, no outline), no fill animation while dragging; `40 km` or `12 of 18 km` `type/caption` `text/secondary` + fare `type/body` 600; dragging a bar selects that town; selected row text `text/primary`, others `text/secondary`, bars stay full color. Computation tile `bg/subtle` `radius/lg`, padding 12 / 16, `space/1` row gap: label `type/caption` `text/secondary` left, value `type/body` 600 right; total row `type/h3`. Footnote `type/caption` `text/secondary`. Prototype: `prototype/fare-card/index.html`) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instance `Fare Card` on `Commuter / 01 Home` |

**Card/Jeepney anatomy** — 320 × 164 (the deck's track and drag wiring depend on this height), `bg/default`, `radius/xl`, `shadow/soft`, no border, 16 px padding, 8 px row gap, 4 px before the footer.

| Row | Content |
|---|---|
| Header | Route chip: fill `route/n` at 16 % with the code in `type/caption` 600 `text/primary` (dark ink, not route ink, so every route clears AA). Destination `type/h3`. ETA right, `type/body` 600. |
| Seat gauge | Occupancy value in `type/body-lg` 700, warning states use `semantic/warning-ink`. 8 dots (8 px, 4 px gap): free = dark (`text/primary`), taken = light gray (`bg/strong`). Every value or state is driver-entered; the freshness stamp is not repeated here (it lives on Home/detail). |
| Meta | Fare and rating only (`type/caption`, star bound to `status/weak`), left-aligned so the row hugs. No freshness text on the card. |
| Footer | "Next stop" `type/caption` + stop name `type/body` 600, then one ghost `Link/SeeMore`: label "See more" `type/body` 600 `accent/default`, 4 px gap, `Icon/chevron-right` at 16 px stroke 1.75 `accent/default`, no fill, no border, no shadow, 44 px touch target. The stop name slot takes the remaining 193 px and truncates with an ellipsis (`textTruncation: ENDING`) so the card height never changes. No bell and no filled button — a comparison card carries one action, and alerts belong on Home. |

No thumbnail: the card reads by route, seats and ETA, which is what a commuter compares across the deck. Never imply seats from GPS — a count is always the driver's last entry, and the "Updated N min ago" freshness line lives on Home/detail rather than on the card.

Full anatomy, variants, motion and clash notes for `Role/Commuter/NearestJeepney`: `design/nearest-jeepney.md`. Read it before working on that card.

**Reusable Figma motion sub-components** (on the Foundations page):
- **`Foundations/DigitColumn`**: Clipped 1-digit window (`Size=Display` `26 × 48` in `type/display` and `Size=Mono` `7 × 15` in `type/mono-body`, no fill) containing an absolutely-positioned `"Column"` frame with digits `9..0` stacked top-to-bottom (`y = -(9 - d) * H`). Variants: `Digit = 0..9` plus `Digit = Blank` (width `0.01`, `y = -9 * H` with `"0"` hidden). Counting down moves `"Column"` upward so the old digit exits upward and the new digit enters from below.
- **`Foundations/ETACountdown`**: Horizontal baseline-aligned auto-layout with `[Tens DigitColumn][Ones DigitColumn]` (`Size=Display`), `"MIN"` (`type/mono-tag`), and hidden `"Arriving"` (`type/display`). `Step = 1..8` (`11, 10, 9, 6, 4, 3, 1, Arriving`) with `AFTER_TIMEOUT` `3000ms` (`2000ms` on `Step=8` back to `Step=1`), Smart Animate `400ms` custom bezier `(0.22, 1, 0.36, 1)`, plus static `Hold=Arriving` and `Hold=Value` variants.
- **`Foundations/SeatsLive`**: 20-dot seat grid (`Seat 1..20`, `8 × 8` dots, `8px` gaps; free = `text/primary`, taken = `bg/strong`), count line `"[Tens DigitColumn][Ones DigitColumn] of 20 seats free"` (`Size=Mono`), and `"DRIVER-REPORTED · 2 MIN AGO"`. `Step = 1..10` (`8, 9, 10, 9, 8, 7, 6, 7, 8, 9` free seats) with `AFTER_TIMEOUT` `4000ms` (out-of-sync with the `3000ms` ETA loop), Smart Animate `400ms` custom bezier `(0.22, 1, 0.36, 1)`, plus static `Hold=Full` and `Hold=Value` variants.
- **`Foundations/LivePulse`**: `6 × 6` live indicator (`Pulse=A` 1x ring at 50% opacity → `Pulse=B` 2.6x `15.6 × 15.6` ring at 0% opacity after `0ms` delay, Smart Animate `2000ms` `EASE_OUT`; `Pulse=B` → `Pulse=A` after `0ms` delay, Instant), placed in `Role/Commuter/CardHeader` (`Tone=Live`). The pulse is a flat translucent circle that fades out, not a stroked ring.

