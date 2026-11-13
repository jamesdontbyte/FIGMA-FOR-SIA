# DESIGN.md: Loc8 Design System

> App name: **Loc8**. Logo: TBD — use `[APP LOGO]` placeholder until final.
> Product: Loc8, a jeepney tracking app with two roles, **Commuter** and **Driver**. A coop/LTFBR/LTO web dashboard comes later and reuses these tokens.

## 0. How to use this file (agents read this first)

- Every component, screen and page MUST use the tokens below. **Never hard-code hex values, font sizes, radii or spacing.**
- **Reuse first.** Use components and assets listed in section 11. Create a new one only when the user explicitly asks.
- If a needed token or component is missing, add it to this file first, then use it.
- Style in one line: **soft minimalist**. White canvas, pastel tints, pill shapes, black primary actions, very little text, visuals first.
- Platform-agnostic: tokens are named for Figma variables and map to any stack.
- Both roles share the same system.

## 1. Principles

1. **Clean, not cluttered.** One focal point per screen, at most 3 to 4 cards above the fold.
2. **Visuals over text.** Numbers, icons, rings, and color chips instead of sentences. One short label per card.
3. **Soft and rounded.** Large radii, light shadows, pastel fills. No hard borders, no heavy gradients.
4. **One black action.** One filled black button per view. Everything else is quieter.
5. **Honest status.** Live, stale and offline states are always visible and never rely on color alone.
6. **Glanceable.** Key values (ETA, seats, status) are the largest thing in their card.

## 2. Color

### 2.1 Core

| Token | Hex | Use |
|---|---|---|
| `bg/default` | `#FFFFFF` | Card and control surface (`#FFFFFF`) |
| `bg/app` | `#F1F1F2` | Warm light-gray screen canvas background (`background.app`) |
| `bg/subtle` | `#F7F8FA` | Grouped sections, page behind cards when needed |
| `bg/muted` | `#F1F3F6` | Inputs, secondary buttons, segmented control track |
| `bg/auth-hero` | `#0A0A0A` | App-ink header behind auth sheets (Login / Sign Up). Figma alias of `primary/default`, so it follows that token automatically |
| `bg/mascot-band` | `#262B35` | Light-black / charcoal band behind the Home mascot hero (`Role/Commuter/MascotHero`). Figma alias of `primary/pressed` |
| `border/default` | `#E6E9EE` | Hairlines, card outlines |
| `border/card-subtle` | `#0000000A` | Ultra-subtle 1 px hairline (`rgba(0,0,0,0.04)`) for small surfaces (search pill on Map, chips, weather pill, notification bell). **Not used on `Role/Commuter/FlatCard` cards — cards are borderless.** |
| `border/strong` | `#D3D8DF` | Dividers, disabled outlines |
| `text/primary` | `#0F1115` | Headings, values |
| `text/secondary` | `#5F6877` | Labels, captions |
| `text/tertiary` | `#8A92A0` | Placeholders, hints (never for essential info) |
| `text/inverse` | `#FFFFFF` | Text on black or accent |
| `primary/default` | `#0A0A0A` | **Primary button**, nav bar, selected segment |
| `primary/pressed` | `#262B35` | Primary pressed |
| `primary/disabled` | `#D3D8DF` | Disabled fill (text `text/tertiary`) |

### 2.2 Accent (blue)

| Token | Hex | Use |
|---|---|---|
| `accent/default` | `#1F6FEB` | Floating action button, links, progress, user location, `cta-button` |
| `accent/pressed` | `#1859C2` | Pressed |
| `accent/tint` | `#E8F1FE` | Accent chips, selected-row backgrounds |

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

### 2.5 Header gradient (hero areas only)

`gradient/sky` (Figma Paint Style): top `#CDE6FA` (`bg/sky-gradient-top`) to bottom `#FFFFFF` (`bg/default`). Used behind the top bar and hero visual on Map. Never on buttons or cards. The Home mascot hero uses `bg/mascot-band` (`#262B35`, aliased to `primary/pressed`) as a flat light-black band (see 4.1).

### 2.6 App-specific colors

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
| `route/1` to `route/6` | `#1F6FEB` `#F28C38` `#2E9E5B` `#8B5CF6` `#14B8A6` `#EC5C9A` | Route colors, assigned per route (e.g., `R1 · Bugasong`, `R2 · San Jose`, `R3 · Patnongon`, `R4 · Belison`, `R5 · Sibalom`, `R6 · Barbaza`). Never red (reserved for errors). |

### 2.7 Map palette (base map surfaces)

| Token | Hex | Use |
|---|---|---|
| `map/water` | `#D9E8F5` | Open sea and deep water on the base map |
| `map/water-shallow` | `#E7F1FA` | Coastal shelf / littoral contour band along the shoreline and estuaries |
| `map/land` | `#F7F4EA` | Land mass fill |
| `map/landcover` | `#E8F0E1` | Soft vegetation and inland terrace patches |
| `map/road-casing` | `#E2DED2` | Casing behind base-map roads (the road core is `bg/default`) |

Rules: base-map surfaces only — never on cards, buttons, chips or nav. One road per map, no labels, no POIs, no pins, no route line. A screen that needs a route draws it above `Map/Base`.

## 3. Typography

**Font family: Plus Jakarta Sans** (weights 400, 500, 600, 700, 800). Fallback: system sans-serif. Support OS font scaling up to 130%.

| Token | Size / Line | Weight | Use |
|---|---|---|---|
| `type/display` | 40 / 48 | 800 | Big numbers (ETA, counters) |
| `type/h1` | 28 / 36 | 700 | Screen titles, hero line |
| `type/h2` | 22 / 30 | 700 | Section titles |
| `type/h3` | 18 / 26 | 600 | Card titles |
| `type/body-lg` | 16 / 24 | 500 | Primary body, buttons |
| `type/body` | 14 / 20 | 400 | Secondary text |
| `type/caption` | 12 / 16 | 500 | Labels, chips, timestamps |
| `type/overline` | 11 / 14 | 600, +4% tracking | Tiny uppercase tags (rare) |
| `type/greeting` | 17 / 24 | 600 | Home greeting title (`"Good morning, Ana"`) |
| `type/mono-tag` | 11 / 14 | 500 (`JetBrains Mono`), +4% tracking | Monospace dates (`"TODAY, 11 NOVEMBER"`), secondary telemetry (`"LIVE · 20S AGO"`, `"DRIVER-REPORTED · 2 MIN AGO"`), and units (`"MIN"`) |
| `type/mono-body` | 11 / 16 | 500 (`JetBrains Mono`) | Monospace seat counts and compact status lines (`"8 of 16 seats free"`, `"J-014 · arriving Plaza"`) |

Rules:
- Max 2 weights per card. Values use 700 or 800, labels use 500.
- Units sit next to the number at `type/body` in `text/secondary` (for example **6** min, **28**°C).
- Sentence case everywhere. No all-caps buttons.
- Keep copy short: titles 1 to 3 words, helper text one line.

## 4. Layout, spacing, shape

### 4.1 Spacing (4pt grid) & Layout Constants

`space/0`=0 · `space/1`=4 · `space/2`=8 · `space/3`=12 · `space/4`=16 · `space/5`=20 · `space/6`=24 · `space/8`=32 · `space/10`=40 · `space/12`=48 · `space/14`=56 · `space/16`=64 · `space/20`=80

**Spec & Layout Tokens (in Spacing collection for 100% variable binding):**
- `layout/frame-width` = **393** · `layout/frame-height` = **852** (Base mobile frame: iPhone 15/16 Pro)
- `layout/safe-top` = **59** · `layout/safe-bottom` = **34** (Device safe areas)
- `layout/nav-clearance` = **104** (Bottom content padding to clear floating nav)
- `layout/touch-min` = **44** · `layout/touch-driver` = **56** (Minimum touch targets)
- `layout/icon-grid` = **24** (Icon grid size)
- `stroke/hairline` = **1** · `stroke/focus` = **1.5** · `stroke/icon` = **1.75** · `stroke/route` = **5** · `stroke/route-casing` = **9** (Stroke weight tokens)
- `size/dot-xs` = **6** · `size/dot-sm` = **8** · `size/dot-md` = **10** · `size/dot-user` = **14**
- `size/checkbox` = **22** · `size/knob` = **28** · `size/switch-h` = **32** · `size/switch-w` = **52**
- `size/handle-w` = **36** · `size/avatar-md` = **40** · `size/avatar-lg` = **64** · `size/control-md` = **48** · `size/input-lg` = **52**
- `size/nav-height` = **64** · `size/quick-tile` = **72** · `size/stat-card-w` = **170** · `size/content-width` = **353**
- `size/zoom-pill-h` = **88** · `size/hero-map-h` = **548** · `size/welcome-sheet-h` = **332**
- `size/onboarding-sheet-h` = **304** · `size/hero-fade-h` = **96** · `size/top-scrim-h` = **120** · `size/progress-seg-w` = **88**
- `size/auth-hero-h` = **280** · `size/auth-hero-copy-w` = **280** · `size/auth-mascot-w` = **130** · `size/auth-mascot-h` = **176**
- `size/confirm-w` = **353** · `size/confirm-h` = **56** · `radius/confirm-idle` = **16** · `radius/confirm-circle` = **28** · `space/confirm-px` = **14** · `size/icon-xs` = **16** · `stroke/check` = **3** · `size/matrix-dot` = **2** · `size/matrix-gap` = **2** · `size/matrix-grid` = **14**
- `size/bell-btn` = **36** · `size/weather-pill-h` = **36** · `size/search-pill-h` = **46** · `size/saved-chip-h` = **32** · `size/home-content-w` = **361** (Home screen uses `space/4` 16 px horizontal margin and fluid `FILL` card width so it scales cleanly from 360 px to 430 px wide)
- `layout/home-top` = **71** (Home content top: `layout/safe-top` 59 + `space/3` 12) · `size/mascot-hero-h` = **160** · `size/mascot-hero-w` = **393** · `size/mascot-band-h` = **84** · `size/mascot-art-w` = **132** · `size/mascot-art-h` = **150** · `size/speech-bubble-w` = **233** · `size/speech-tail-w` = **14** · `size/speech-tail-h` = **16**

- Screen horizontal padding: **20** (`space/5`)
- Card inner padding: **16** (`space/4`, stat tiles) or **20** (`space/5`, feature cards)
- Gap between cards: **12** (`space/3`). Gap between sections: **24** (`space/6`).
- Bottom content padding: **104** (`layout/nav-clearance`, clears the floating nav)
- Auth header (`bg/auth-hero` → `primary/default` ink, Login / Sign Up): title `text/inverse`, subtitle `bg/sky-gradient-top`; fixed height `size/auth-hero-h` (280), top padding `layout/safe-top` (59), copy top-aligned (16 px heading inset, title-to-subtitle gap `space/2` 8). Title and subtitle are capped at `size/auth-hero-copy-w` (280).
- Auth mascot (`Login / Mascot`): `Reference/mascot2.jpg` (black background removed), `size/auth-mascot-w` × `size/auth-mascot-h` (130 × 176), peeking in from the right edge: 40 px (`space/10`) of its width is clipped by the screen frame, feet overlapping the sheet top by `space/2` (8). Layered above the sheet. One mascot per screen, never on cards or buttons.
- Auth form shape consistency: on auth sheets, the role segmented control track, and the primary submit button use `radius/md` (16) to match the text fields; selected/inactive segments use `radius/sm` (12). The auth role selector (`Control/RoleSelect`) uses a white `bg/default` indicator with `shadow/soft` and `text/primary` label, inset 8 px (`space/2`) inside a 56 px track, so the submit button stays the only black fill on the sheet. Icon-only social buttons stay circular.
- Auth shell per role: Login ships as two frames, `Welcome Back` (Commuter) and `Welcome Back / Driver`. Both are the same 393 × 852 vertical auto-layout shell — header 280, form sheet, mascot — cloned rather than rebuilt. Only two things differ: which `Control/RoleSelect` variant is selected (Driver starts on `Role=Driver`) and the subtitle copy ("Sign in to see live jeepneys near you." vs "Sign in to go online and manage your trips."). Switching chips swaps the variant in place via the component's own 200 ms Smart Animate, and on the two real screens the chip is overridden at instance level to navigate to the other role's frame instead (Smart Animate 200 ms ease-out, `Chip/Driver` on Commuter → `Welcome Back / Driver`, `Chip/Commuter` on Driver → `Welcome Back`). The override lives on the instance, so the `Control/RoleSelect` component keeps its in-place `CHANGE_TO` behaviour for any context that has no second frame. Tapping the already-selected chip does nothing. Any further auth screen (Sign Up, OTP) should clone this shell.
- Always respect device safe areas (`layout/safe-top`=59, `layout/safe-bottom`=34).
- Home header order, top to bottom: `Role/Commuter/GreetingRow` at `layout/home-top` (71) → `Role/Commuter/MascotHero` → cards. The greeting row carries the date overline + greeting on the left and the weather pill + notification bell on the right, flush left at `space/0`; **there is no calendar icon box**. Home has **no search bar and no saved-place chips** (`Home` / `School` / `Work`) — search lives on Map — so the first card sits `space/3` (12) under the hero.
- Home mascot hero (`Role/Commuter/MascotHero`): full-bleed `size/mascot-hero-w` 393 × `size/mascot-hero-h` 160 (`clipsContent: true`), edge to edge on `bg/app`, no radius and no shadow. A flat light-black band in `bg/mascot-band` `#262B35` (alias of `primary/pressed`) fills the lower `size/mascot-band-h` 84 px (y 76 to 160). Half-body waving mascot artwork (`Reference/mascotHome.png` cropped to tight bounds in `Reference/homepageMascot-cutout.png`, `size/mascot-art-w` 132 × `size/mascot-art-h` 150) sits at x `-4`, y `14`, flush with the band's bottom edge at y 160. Speech bubble: compact white `bg/default`, `radius/lg` 20, `size/speech-bubble-w` 233 × 90 at x 132, y 54, `space/3` 12 vertical / `space/4` 16 horizontal padding, `space/1` 4 gap, `shadow/card`, with a left-pointing `Bubble Tail` vector (`size/speech-tail-w` 14 × `size/speech-tail-h` 16 at x 120, y 112, `bg/default`) pointing toward the mascot; label `LOC8` in `type/overline` `bg/mascot-band` (`#262B35`, matching the light-black band), 3-line message in `type/caption` `text/secondary` (`"Welcome, Ana! I'm Loc8. I'll help you track live jeepneys, free seats, and arrival times in one place."`). One mascot hero per screen, never inside a card.

### 4.2 Radius

| Token | px | Use |
|---|---|---|
| `radius/xs` | 7 | Checkbox, micro tags |
| `radius/sm` | 12 | Small chips, thumbnails |
| `radius/md` | 16 | Inputs, list rows, dropdown menus |
| `radius/lg` | 20 | Stat tiles |
| `radius/xl` | 24 | Cards |
| `radius/2xl` | 28 | Bottom sheets (top corners) |
| `radius/pill` | 999 | Buttons, chips, nav, search, segmented control |

### 4.3 Elevation

| Token | Value | Use |
|---|---|---|
| `shadow/card` | `0 2 12 rgba(0,0,0,0.04)` | Flat white cards, mascot speech bubble, weather pill, and notification bell button on `bg/app` (`#F1F1F2`) |
| `shadow/soft` | `0 4 16 rgba(15,17,21,0.06)` | White cards on white or gradient |
| `shadow/raised` | `0 8 24 rgba(15,17,21,0.10)` | Sheets, menus, hero-overlap cards |
| `shadow/nav` | `0 8 24 rgba(0,0,0,0.18)` | Floating nav pill |

Use hairline `border/default` OR `shadow/soft` on a white card, not both heavy.

### 4.4 Glass (optional, restrained)

Only for small chips floating over map or hero images: white at 70% opacity with 16 px background blur. Never for full cards or text-heavy areas.

## 5. Iconography and imagery

- Icon style: **outline, 1.75 stroke, rounded caps and joins, 24 px** (Lucide-style). Active nav icons use the filled variant.
- Icons in tinted circles: 44 px circle with pastel fill and its ink color for the icon.
- Key icons: home, map, start (play) / end (stop square), flame (hotspots), user-circle, bell, pin, bus/jeepney, seat, shield (SOS), clock, cloud (weather).
- Hero visual: flat vector illustration, soft shadows, route-colored jeepney. Transparent PNG/SVG, placed top-right and slightly cropped by the screen edge. Its wheels overlap the first card's top edge by about 24 px.
- Loc8 mascot: a navy VR-helmet rider with an `8` keychain. Home uses `Reference/mascotHome.png` (tightly cropped in `Reference/homepageMascot-cutout.png`) in the `Role/Commuter/MascotHero` band; auth screens and the Activity empty state use `Reference/mascot2.jpg`. Brand-color artwork — an intentional exception to the token palette, never recolored, never redrawn.
- Avatars: circle, 40 px (list) or 64 px (profile).
- No stock photos of people in core flows.

## 6. Components

All components define default, pressed, disabled, and (where relevant) loading states. Minimum touch target **44 x 44** (driver mode: **56**).

### 6.1 Buttons

| Component | Spec |
|---|---|
| **primarybutton** | Pill, height 56 (large) / 48 (medium) / 40 (small). Fill `primary/default`, text `text/inverse` at `body-lg` 600. Pressed `primary/pressed` and scale 0.98. Disabled `primary/disabled`. Loading: spinner replaces label, width stays. Full width in forms and sheets. |
| **secondarybutton** | Same sizes. Fill `bg/muted`, text `text/primary`, no border. Outline variant: transparent, 1 px `border/strong`. Optional leading brand logo (`Has Logo` boolean + `Logo` INSTANCE_SWAP, hidden by default; logo 24 / 20 / 16 px for Large / Medium / Small). Social sign-in uses this with `Logo/Google` and `Logo/Facebook`. |
| **iconbutton** | 44 px circle, white fill, `shadow/soft`, icon 22 px. On gradient headers it stays white. Notification badge: 8 px `error` dot, or count pill (min 18 px) at top-right. |
| **floatingbutton** | 56 px circle, `accent/default`, white icon 26 px, `shadow/raised`. Used for the center nav action and map recenter (recenter is 44 px, white). Stop/End state uses `error` ink `#D93036`. |
| **cta-button** | Pill 56, fill `accent/default`, white text, optional trailing chevrons. For the single hero action (onboarding Next, empty-state action). Do not show next to a primarybutton on the same view. |
| **togglebutton** | Two forms. **Segmented**: track `bg/muted` pill, height 44, selected segment `primary/default` with white text, 200 ms slide. **Switch**: 52 x 32 track (`size/switch-w` × `size/switch-h`), 24 px white circle knob (`layout/icon-grid`) with 4 px (`space/1`) equal inset border clearance on all sides (`32 - 2×4 = 24 px`), on `primary/default`, off `border/strong`. |
| **dropdownbutton** | Pill, height 44, white fill, 1 px `border/default`, label + chevron-down 18 px. Opens a menu (`radius/md`, `shadow/raised`) or a bottom sheet on mobile. |
| **confirmbutton** (`Button/Confirm`) | Interactive morphing button inside a full-width centered flex wrapper (`.confirm-wrap { display: flex; justify-content: center; align-items: center; width: 100%; }` — fixed/full section width, never shrink-to-fit, no `margin-left: 0`, `align-self: flex-start`, or `text-align: left`, so left and right edges collapse inward and expand outward symmetrically from the center). Button pill (`size/confirm-w` 353 × `size/confirm-h` 56, `radius/confirm-idle` 16 [`radius/md`], fill `primary/default` [`--stage-accent`], centered `"Verify"` label in `text/inverse` [`--stage-on-accent`] at `type/body-lg` [Plus Jakarta Sans 16 px / 24 px SemiBold], `shadow/soft`, horizontal padding `space/confirm-px` 14, `-webkit-font-smoothing: antialiased`, `text-rendering: optimizeLegibility`). Tapping sets `data-animating` (`will-change: transform, opacity, filter, width, border-radius` on button and children only while `[data-animating]` is present) and shrinks width symmetrically toward the center from measured `idleW` (`size/confirm-w` 353) → `size/confirm-h` × `size/confirm-h` (56 × 56 perfect circle, collapsed width derived from `--confirm-h`, never hardcoded) while animating `border-radius` from `radius/confirm-idle` (16 px) → `radius/confirm-circle` (28 px, `calc(var(--confirm-h) / 2)`) over **300 ms** `cubic-bezier(0.22, 1, 0.36, 1)` (`padding: 0`), fading out the centered `"Verify"` label (**250 ms** `ease-in-out`, `opacity: 0`, `filter: blur(2px)`, `transform: none` — no scale on hidden label so browser does not retain a low-res raster layer) into a 4×4 rounded dot-matrix orbit loader (`size/matrix-grid` 14 × 14, `size/matrix-dot` 2 px dots, `size/matrix-gap` 2 px gap; corners `[0, 3, 12, 15]` hidden, 8 perimeter dots `[1, 2, 7, 11, 14, 13, 8, 4]` pulsing clockwise from 35% to 100% `text/inverse` on a **1200 ms** `ease-in-out` cycle, center 4 dots at 35% `text/inverse`) for **2000 ms** (`aria-label="Verifying"`, `aria-busy="true"`), then swapping (**250 ms** `ease-in-out`, hidden icons use `opacity: 0`, `filter: blur(2px)`, `transform: scale(0.25)`; visible/resting state on label, loader, and check uses `opacity: 1`, `filter: none`, `transform: none` instead of `blur(0)` / `scale(1)`) to a 16 px check icon (`size/icon-xs` 16, `stroke/check` 3, rounded caps, `text/inverse`, `aria-label="Verified"`) for **1400 ms** before expanding symmetrically outward from the center back to measured `idleW` (`353px`) and `radius/confirm-idle` (`16px`) `Idle` (`aria-label="Verify"`) over **300 ms** `cubic-bezier(0.22, 1, 0.36, 1)`, then clearing inline `width`, `disabled`, and `data-animating` after `--resize-dur` (300 ms). Press state uses `primary/pressed` and scale `0.97` over **150 ms** `cubic-bezier(0.22, 1, 0.36, 1)` (held ≥150 ms on touch). Hover (mouse only): `brightness(1.15)`. Focus ring: 2 px `bg/default` (`--stage-surface`) gap + 2 px `primary/default` (`--stage-accent`) ring. Reduced-motion (`prefers-reduced-motion: reduce`): removes all transitions and animations; state changes occur instantly. |

### 6.2 Navigation

| Component | Spec |
|---|---|
| **topbar** | Height 56 + safe area. Transparent over `gradient/sky`. Left: `[APP LOGO]` (or back iconbutton on inner screens). Right: iconbuttons (bell, filter). Centered title (`h3`) on inner screens. |
| **stickynavbar** | A topbar that gains `bg/default` at 90% opacity + hairline `border/default` once content scrolls under it. |
| **bottombar** | Floating pill: fill `primary/default`, height 64, radius pill, 16 px side margin, 12 px above safe area, `shadow/nav`. Icons 24 px, inactive white at 60%. Active item: white circle (or pill with label) with black icon. The center slot may hold a raised **floatingbutton** (Waiting for commuters, Start/End Trip for drivers). Max 5 items. |
| **hamburgermenu / sidebar / collapsiblesidebar / megamenu / breadcrumbs / navbar / footer** | **Not used in the mobile app.** Reserved for the coop/LTFRB/LTO web dashboard and landing site, using the same tokens. |

### 6.3 Sections (mobile adaptations)

| Component | Spec |
|---|---|
| **herosection** | Gradient sky behind the topbar, large vehicle/illustration overlapping the first card. Onboarding hero: illustration + 1-line title (`h1`) + one helper line. |
| **featuressection / benefitssection** | Onboarding slides and info cards: 3 slides max, one illustration + title + one line each, page dots (active dot = 20 px pill `primary/default`, inactive 6 px circle `border/strong`), Skip (secondarybutton small) and Next (cta-button). |
| **aboutsection** | App name, version, Terms and Privacy links as list rows. |
| **faqsection** | Collapsible rows: question `body-lg` 600, chevron rotates, answer `body` `text/secondary`. 16 px row padding, hairline dividers. |
| **contactsection** | Rows with tinted icon circles (message coop, report a problem, call). |
| **servicessection / teamsection / testimonials / reviewssection** | Web/landing only. |

### 6.4 Cards and surfaces

| Component | Spec |
|---|---|
| **Card (white)** | `bg/default`, `radius/xl`, padding 16 to 20, `shadow/soft` or hairline. |
| **Stat tile** | Tinted fill, `radius/lg`, padding 16. Label `caption` secondary, value `display` or `h1`, unit `body`. Optional 44 px icon circle top-right. |
| **List row** | Height 64, 44 px icon circle (tinted), title `body-lg` 600, subtitle `caption` secondary, trailing value or chevron. |
| **Bottom sheet** | White, top radius `radius/2xl`, 36 x 4 handle `border/strong`, scrim `rgba(0,0,0,0.4)`, `shadow/raised`. |
| **Chip / badge** | Height 28, pill, `caption` 600, semantic or tint fill with matching ink. Optional 8 px leading dot. |

### 6.5 Inputs

- Text field: height 56, `radius/md`, fill `bg/muted`, no border. Focus: 1.5 px `primary/default` border. Error: 1.5 px `error` ink + helper text in error ink. Label above (`caption` 600), placeholder `text/tertiary`.
- Search: pill, height 52, leading search icon, fill white with `shadow/soft`. Map only — Home has no search bar (see 4.1).
- OTP: 4 boxes, 48 x 56, `radius/md`, fill `bg/muted`, focused box has black border (no cursor inside the box). Resend countdown in `caption` secondary.
- Date picker field: same as text field with a calendar icon.
- Checkbox: 22 px, `radius` 7, checked = black fill with white tick.

### 6.6 Feedback

- Toast: pill at top, `primary/default` fill, white text, 3 s.
- Banner: full-width card with semantic fill and ink, icon left, one line, optional action.
- Empty state: 160 px illustration + one `h3` line + one cta-button.
- Skeleton: `bg/muted` blocks with soft shimmer.

## 7. Motion

- Standard UI (buttons, chips, toggles): 200 ms ease-out. Sheets: 320 ms spring (damping about 0.85).
- Press: scale 0.98 and light haptic on primary actions.
- Marker movement: interpolate between GPS fixes over about 1 s, linear.
- Bottom nav: keep the current nav bar motion unchanged.

### Page switch: staggered cascade
When the user switches pages, the new page builds in piece by piece, top to bottom.
- Old page: exits almost instantly, opacity 1 to 0 in 80 ms, no slide or scale.
- New page: the top bar and header area appear first, with no delay.
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

## 8. Accessibility

- Contrast: body text at least 4.5:1, large text and icons at least 3:1. Do not use `text/tertiary` for essential info.
- Touch targets at least 44 px (driver mode 56 px).
- Never use color alone: pair every status color with an icon or label.
- Support dynamic type, screen readers (labels on all iconbuttons), and one-hand reach (primary actions in the lower half).
- Moving-vehicle safety: no typing, no scrolling lists, and no multi-step flows while the driver is moving.

## 9. Do and don't

**Do**
- Keep white space generous; one idea per card.
- Use big numbers with small units.
- Use pastel tints to group by meaning (Sky = time, Mint = money, Lime = ready, Peach = alerts).
- Keep the bottom nav to 5 items, with one raised center action at most.

**Don't**
- Don't use more than one filled black button per view.
- Don't put gradients on buttons or cards.
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

**Theme Mode:** Light mode only (`Light` mode in variable collections).
**Base Mobile Frame:** `393 x 852` (with `59 px` top safe area, `34 px` bottom safe area, `20 px` side padding, `104 px` bottom nav clearance).

Create these variable collections to match the tokens above:
1. **Color** (`Light` mode): groups `bg`, `text`, `border`, `primary`, `accent`, `tint`, `semantic`, `status`, `demand`, `route` (plus `gradient/sky` Paint Style).
2. **Typography**: text styles named `type/display` through `type/overline` using Plus Jakarta Sans.
3. **Spacing** (`Light` mode): numeric variables `space/0` to `space/20`, plus `layout/*`, `stroke/*`, and `size/*` tokens so zero values are hard-coded.
4. **Radius** (`Light` mode): numeric variables `radius/none` (0) and `radius/xs` to `radius/pill`.
5. **Effects**: styles `shadow/soft`, `shadow/raised`, `shadow/nav`.

Component naming: `Button/Primary/Large/Default`, `Chip/Success`, `Card/Stat/Sky`, `Nav/Bottom/Active-Home`. Use auto layout everywhere and variants for states.

## 11. Component and asset registry (reuse these)

| Need | Use this | Where |
|---|---|---|
| Route label | `Badge/Route` | Foundations |
| GPS status | `Chip/GPS` | Foundations |
| Tinted icon | `IconCircle/Tint` | Foundations |
| Bottom nav (commuter) | `Floating Commuter Nav` | Foundations |
| Buttons | `Button/Primary/{Large,Medium,Small}/{Default,Pressed,Disabled}` | Foundations |
| Jeepney transit card | `Card/Jeepney` (`Route=R1`…`Route=R6`; 320 × 164, occupancy-first — see anatomy below) | Foundations (Components / 04) |
| Interactive swipe deck | `Card/JeepneyCarousel` (`Active=1`…`Active=6`; each variant is 393 × 852 — a 2× `Map/Base` viewport panned to that route's jeepney plus the card track at `y = 570`, so the 320 × 164 card bottom sits at `734`, `space/5` (20 px) above the nav top at `754`. No pagination dots, drag handle or slider cue — the deck is read from the cards themselves and the jeepney markers; drag left = next, drag right = previous, clamped at the ends; tapping a card or a jeepney marker switches state) | Foundations — 6-variant master strip on a page-level shelf beside Components / 04 (must stay in one horizontal row for drag direction), plus a live 393 px demo instance inside the deck section |
| Full-screen label-free base map | `Map/Base` (393 × 852, edge to edge, no labels, one road, 6 live jeepney markers bound to `route/1`…`route/6`) | Foundations — Components / 05 Map |
| Social brand logos | `Logo/Google`, `Logo/Facebook`, `Logo/Apple` (24 px, fixed brand colors — intentional exception, not token-bound) | Foundations — Section: Logo/* (in Components / 01 Primitives & Status) |
| App mascot | `Login / Mascot` image frame (`Reference/mascot2.jpg` with the black background removed, FIT; 130 × 176 on auth screens, 160 × 160 on Commuter Activity empty state; brand-color artwork, intentional exception, not token-bound). Home uses the same character waving in `Role/Commuter/MascotHero`, from `Reference/mascotHome.png` (`Reference/homepageMascot-cutout.png`) | Login screens `Welcome Back`, `Welcome Back / Driver`, `Create Account` (page Login-Signup-OTP-Terms-Privacy), `Commuter / 03 Activity / Empty` and `Commuter / 01 Home` (page Commuter) |
| Auth role selector | `Control/RoleSelect` (`Role=Commuter` / `Role=Driver`; 353 × 56 (`space/14`) track `bg/muted` `radius/md`, chips keep a 48 px hit area; sliding `Indicator` `bg/default` + `shadow/soft`, `radius/sm`, inset 8 px (`space/2`); active ink `text/primary`, inactive `text/secondary`). Prototype: tapping the inactive chip changes to the other variant, Smart Animate 200 ms ease-out | Foundations — Components / 02, section after Control/Segmented. Instances on `Welcome Back` (Commuter) and `Welcome Back / Driver`, each overriding the inactive chip to navigate to the other frame instead of swapping in place |
| Activity trip history row | `Card/Trip` (353 × 140, `bg/default`, `radius/lg`, 1 px `border/default`, 16 px padding, 12 px row gap; header: `Badge/Route` instance + fare `type/h3` right; meta: calendar + `Date#836:1`, jeepney + `Jeepney ID#836:2`, clock + `Wait time#836:3` in `type/caption` `text/secondary`; footer: 44 px hit-area actions `Rebook` in `accent/default`, `Report issue` in `text/secondary`, `Details` + chevron right) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instances on `Commuter / 03 Activity / History` |
| Morphing confirm button | `Button/Confirm` (`State=Idle`, `State=Pressed`, `State=Loading 1`…`State=Loading 8`, `State=Done`; 353 × 56 `radius/confirm-idle` 16 `primary/default` + `text/inverse` + `shadow/soft` shrinking to 56 × 56 circle (`radius/confirm-circle` 28) with 14 × 14 4×4 orbit dot loader and 16 px stroke-3 `Icon/check`, then returning to 353 × 56; label TEXT property, default `Verify`) | Foundations — Components / 02 Buttons & Controls. Instance `Button / Verify` on `Verify Account` (`OTP / Actions` slot, replaces the old `Button/Primary/Large`) |
| Commuter Home greeting row | `Role/Commuter/GreetingRow` (361 × 40, no icon box: stacked `Date#946:0` `"TODAY, 11 NOVEMBER"` in `type/mono-tag` and `Greeting#946:1` `"Good morning, Ana"` in `type/greeting` left, starting flush at x 0; white `Weather Pill` `Icon/cloud` + `28°` and 36 × 36 circular `Button/NotificationBell` with `Icon/bell` + unread dot right; all surfaces use `shadow/card` and 1 px `border/card-subtle`) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instance on `Commuter / 01 Home` |
| Home mascot hero | `Role/Commuter/MascotHero` (393 × 160 full-bleed, `clipsContent: true`; flat light-black `bg/mascot-band` `#262B35` band 393 × 84 at y 76, no radius, no shadow; half-body waving mascot artwork 132 × 150 at x -4, y 14 flush with the band bottom; compact white `radius/lg` 20 speech bubble 233 × 90 at x 132, y 54 with left-pointing `Bubble Tail` 14 × 16 at x 120, y 112, `space/3` 12 vertical / `space/4` 16 horizontal padding, `space/1` 4 gap, `shadow/card`, label `LOC8` in `type/overline` `bg/mascot-band` + 3-line message `type/caption` `text/secondary`; `Message#964:0` TEXT property) | Foundations — Commuter Components Row 4, instance `Mascot Hero` on `Commuter / 01 Home` |
| Waving mascot | `Mascot/Wave` (132 × 148, animated GIF fill; GIF plays continuously in Figma Presentation/Prototype view; static resting pose in editor mode) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), component `1096:6119` |
| Flat card header row | `Role/Commuter/CardHeader` (`Tone=Live` green `status/live` dot / `Tone=Explore` blue `accent/default` dot + `Title#946:2` in `text/secondary` 13/18 Medium left; `Meta#946:5` in `type/mono-tag` `text/tertiary` + 16 px `Icon/arrow-right` right, with `Show Meta#946:8` and `Show Arrow#946:11` booleans) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instances across `Commuter / 01 Home` cards |
| Flat white card surface | `Role/Commuter/FlatCard` (`bg/default` `#FFFFFF`, `radius/xl` 24, `space/4` 16 px inner padding, **no border/stroke**, `shadow/card` `0 2px 12px rgba(0,0,0,0.04)`) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), used across `Commuter / 01 Home` on `bg/app` (`#F1F1F2`) |
| Nearest jeepney card | `Role/Commuter/NearestJeepney` (`State=Live` 361 × 320 across `Route=R1` / `R2` / `R3` and `Alert on=Off` / `On`, `State=Arriving` 361 × 298, `State=Full` 361 × 320, `State=No jeepneys` 361 × 188, `State=Loading` 361 × 320, plus `State=Pressed Track` and `State=Pressed Alert` 361 × 320; props `ETA#1000:6`, `Sub line#1000:12`, `Seats free#1000:18`, `Updated#1000:24` (TEXT), `Route`, `Alert on`, `State` (VARIANT); interactive HTML/CSS/JS motion prototype at `prototype/nearest-jeepney-card/index.html`; anatomy and motion below) | Foundations — Section: Commuter Role Components (`Role/Commuter/*`), instance `Card/NearestJeepney` on `Commuter / 01 Home` |

**Card/Jeepney anatomy** — 320 × 164 (the deck's track and drag wiring depend on this height), `bg/default`, `radius/xl`, `shadow/soft`, 16 px padding, 8 px row gap, 4 px before the footer.

| Row | Content |
|---|---|
| Header | Route chip: fill `route/n` at 16 % with the code in `type/caption` 600 `text/primary` (dark ink, not route ink, so every route clears AA). Destination `type/h3`. ETA right, `type/body` 600. |
| Seat gauge | Occupancy value in `type/body-lg` 700, warning states use `semantic/warning-ink`. 8 dots (8 px, 4 px gap): free = dark (`text/primary`), taken = light gray (`border/strong`). Every value or state is driver-entered; the freshness stamp is not repeated here (it lives on Home/detail). |
| Meta | Fare and rating only (`type/caption`, star bound to `status/weak`), left-aligned so the row hugs. No freshness text on the card. |
| Footer | "Next stop" `type/caption` + stop name `type/body` 600, then one ghost `Link/SeeMore`: label "See more" `type/body` 600 `accent/default`, 4 px gap, `Icon/chevron-right` at 16 px stroke 1.75 `accent/default`, no fill, no border, no shadow, 44 px touch target. The stop name slot takes the remaining 193 px and truncates with an ellipsis (`textTruncation: ENDING`) so the card height never changes. No bell and no filled button — a comparison card carries one action, and alerts belong on Home. |

No thumbnail: the card reads by route, seats and ETA, which is what a commuter compares across the deck. Never imply seats from GPS — a count is always the driver's last entry, and the "Updated N min ago" freshness line lives on Home/detail rather than on the card.

**Role/Commuter/NearestJeepney anatomy and motion** — 361 wide, prop/state driven (`setEta(n)`, `setSeats(array, capacity)`, `selectRoute(id)`, `setAlert(bool)`). The executable reference for all motion is **`prototype/nearest-jeepney-card/index.html`**. Header is `Role/Commuter/CardHeader` (`Tone=Live`, title `Nearest jeepney`, meta `5 ACTIVE · LIVE · 20S`); below it a route chip row of `Badge/Route` instances (`R1 · Bugasong`, `R2 · San Jose`, `R3 · Patnongon`) with one `Indicator` pill (`primary/default` `#0A0A0A`, `radius/pill`, selected chip label in `text/inverse`) that slides under the selected route; then the ETA (`type/display` 40/48 weight 800 number + `MIN` in `type/mono-tag`), the sub line (`J-014 · arriving Plaza` in `type/mono-body`), the 20-dot seat grid (`size/dot-sm` 8 px dots, 10 per row, `space/2` 8 px gap — free = dark `text/primary`, taken = light gray `border/strong`), the count line (`8 of 20 seats free`) and the freshness line (`DRIVER-REPORTED · 2 MIN AGO`), then the action row: `Button/Primary` "Track Jeepney" + `Button/Secondary` "Alert me" in an `Alert Slot`.

| Variant | Size | Shows |
|---|---|---|
| `State=Live, Route=R1/R2/R3, Alert on=Off/On` | 361 × 320 | Full card per route (`R1`: ETA 6, `J-014 · arriving Plaza`, 8/20 free; `R2`: ETA 3, `J-021 · arriving San Jose`, 12/20 free; `R3`: ETA 11, `J-007 · arriving Market`, 0/20 `Full`), wired with Smart Animate between routes and alert states |
| `State=Arriving, Route=R1, Alert on=Off` | 361 × 298 | ETA slot reads `Arriving` (`type/h3` 18/26 SemiBold, ETA under 1 min), unit label hidden |
| `State=Full, Route=R1, Alert on=Off` | 361 × 320 | Count line reads `Full` (0 free seats), every seat dot in `border/strong` |
| `State=No jeepneys, Route=R1, Alert on=Off` | 361 × 188 | Chips stay, body copy "No jeepneys on this route right now", `Track Jeepney` disabled, alert still available |
| `State=Loading, Route=R1, Alert on=Off` | 361 × 320 | `bg/muted` skeletons in every slot, header title `Nearest jeepney` retained |
| `State=Pressed Track / Pressed Alert` | 361 × 320 | `WHILE_PRESSING` (`ON_PRESS`) target scaling `Button/Track` or `Alert Slot` to 97 % over 150 ms |

`Alert on=On` swaps the outlined alert button for an absolutely positioned `Alert On Layer` (145 × 40, `bg/muted`, no stroke, `Icon/bell` + "Alerts on") sitting above it inside `Alert Slot` — the outlined button's white fill hides any layer placed behind it. Seat counts are always the driver's last entry, capped at 20 dots; ETA under 1 min becomes `Arriving`; long route labels truncate with an ENDING ellipsis and never wrap the chip row; extra chips scroll horizontally with the `Indicator` following the selection.

**Reusable Figma motion sub-components** (on `0:1 Foundations` inside `25:72`):
- **`Foundations/DigitColumn`** (`1046:3661`): Clipped 1-digit window (`Size=Display` `26 × 48` in `type/display` and `Size=Mono` `7 × 15` in `type/mono-md`, no fill) containing an absolutely-positioned `"Column"` frame with digits `9..0` stacked top-to-bottom (`y = -(9 - d) * H`). Variants: `Digit = 0..9` plus `Digit = Blank` (width `0.01`, `y = -9 * H` with `"0"` hidden). Counting down moves `"Column"` upward so the old digit exits upward and the new digit enters from below.
- **`Foundations/ETACountdown`** (`1047:3697`): Horizontal baseline-aligned auto-layout with `[Tens DigitColumn][Ones DigitColumn]` (`Size=Display`), `"MIN"` (`type/mono-tag`), and hidden `"Arriving"` (`type/display`). `Step = 1..8` (`11, 10, 9, 6, 4, 3, 1, Arriving`) with `AFTER_TIMEOUT` `3000ms` (`2000ms` on `Step=8` back to `Step=1`), Smart Animate `400ms` custom bezier `(0.22, 1, 0.36, 1)`, plus static `Hold=Arriving` and `Hold=Value` variants.
- **`Foundations/SeatsLive`** (`1047:4330`): 20-dot seat grid (`Seat 1..20`, `8 × 8` dots, `8px` gaps; free = `text/primary`, taken = `border/strong`), count line `"[Tens DigitColumn][Ones DigitColumn] of 20 seats free"` (`Size=Mono`), and `"DRIVER-REPORTED · 2 MIN AGO"`. `Step = 1..10` (`8, 9, 10, 9, 8, 7, 6, 7, 8, 9` free seats) with `AFTER_TIMEOUT` `4000ms` (out-of-sync with the `3000ms` ETA loop), Smart Animate `400ms` custom bezier `(0.22, 1, 0.36, 1)`, plus static `Hold=Full` and `Hold=Value` variants.
- **`Foundations/LivePulse`** (`1046:3668`): `6 × 6` live indicator (`Pulse=A` 1x ring at 50% opacity → `Pulse=B` 2.6x `15.6 × 15.6` ring at 0% opacity after `0ms` delay, Smart Animate `2000ms` `EASE_OUT`; `Pulse=B` → `Pulse=A` after `0ms` delay, Instant), placed in `Role/Commuter/CardHeader` (`Tone=Live`).

**Motion specification** (HTML reference: `prototype/nearest-jeepney-card/index.html`; Figma prototype runs `Foundations/LivePulse`, `Foundations/ETACountdown`, `Foundations/SeatsLive`, route chip slide, alert toggle, and button press states via Smart Animate):

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

Accessibility: `aria-pressed` on route chips and the alert toggle, `role="img"` with a dynamic `aria-label` (`"N of M seats free"`) on the seat dots grid, `aria-live="polite"` on the ETA and `Arriving` line, visible focus rings, 44 px minimum touch hit areas on chips and buttons, and no reliance on seat-dot color alone (the count line carries the meaning).

Clash notes — where the prototype and this file disagreed, this file won:
1. ETA is 60/70 px in the prototype; here it is `type/display` (40/48, weight 800) so the card clears the 361 grid.
2. Card padding 24 px becomes `space/4` 16 px and internal card row gap 24 px becomes `space/4` 16 px, matching `FlatCard` and the other Home cards.
3. The prototype's lowercase "min" unit becomes `MIN` in `type/mono-tag`.
4. The title row is `Role/Commuter/CardHeader`, so the prototype's separate "5 active" counter is folded into its meta string as `5 ACTIVE · LIVE · 20S` (uppercase mono per `type/mono-tag`).
5. Prototype buttons (36 px, 20 px radius) become the shared `Button/Primary` / `Button/Secondary` Small (40 px, `radius/pill`).
6. Seat dots use free = dark (`text/primary`) and taken = light gray (`border/strong`) across both `Role/Commuter/NearestJeepney` and `Card/Jeepney`.
7. The alert on-state uses `bg/muted` + "Alerts on" rather than the prototype's accent-filled toggle, because `accent` is reserved for live/go/location and the filled black button is already spent on `Track Jeepney`.


### Token snapshot (reference)

```json
{
  "color": {
    "bg": { "default": "#FFFFFF", "app": "#F1F1F2", "subtle": "#F7F8FA", "muted": "#F1F3F6", "sky-gradient-top": "#CDE6FA", "auth-hero": "#0A0A0A", "mascot-band": "#262B35" },
    "text": { "primary": "#0F1115", "secondary": "#5F6877", "tertiary": "#8A92A0", "inverse": "#FFFFFF" },
    "primary": { "default": "#0A0A0A", "pressed": "#262B35", "disabled": "#D3D8DF" },
    "accent": { "default": "#1F6FEB", "pressed": "#1859C2", "tint": "#E8F1FE" },
    "border": { "default": "#E6E9EE", "strong": "#D3D8DF", "card-subtle": "#0000000A" },
    "tint": {
      "sky-fill": "#E1EFFB", "sky-ink": "#1F6FEB",
      "lavender-fill": "#EDE7F8", "lavender-ink": "#6B4FB3",
      "mint-fill": "#DFF3E4", "mint-ink": "#2E8B57",
      "peach-fill": "#FDE9DF", "peach-ink": "#D2622B",
      "butter-fill": "#FFF4CF", "butter-ink": "#A87A00",
      "lime-fill": "#E2F5B8", "lime-ink": "#4F7A12"
    },
    "semantic": {
      "success-fill": "#E3F5EA", "success-ink": "#1E8E4F",
      "warning-fill": "#FFF4D6", "warning-ink": "#9A6700",
      "error-fill": "#FDECEC", "error-ink": "#D93036",
      "info-fill": "#E8F1FE", "info-ink": "#1F6FEB"
    },
    "status": { "live": "#2E9E5B", "weak": "#F5A524", "lost": "#E5484D", "stale": "#8A92A080" },
    "demand": { "low": "#4CC38A", "medium": "#F5C542", "high": "#F28C38", "peak": "#E5484D" },
    "route": { "1": "#1F6FEB", "2": "#F28C38", "3": "#2E9E5B", "4": "#8B5CF6", "5": "#14B8A6", "6": "#EC5C9A" },
    "map": { "water": "#D9E8F5", "water-shallow": "#E7F1FA", "land": "#F7F4EA", "landcover": "#E8F0E1", "road-casing": "#E2DED2" }
  },
  "font": { "family": "Plus Jakarta Sans", "weights": [400, 500, 600, 700, 800] },
  "radius": { "none": 0, "xs": 7, "sm": 12, "md": 16, "lg": 20, "xl": 24, "2xl": 28, "pill": 999 },
  "space": { "0": 0, "1": 4, "2": 8, "3": 12, "4": 16, "5": 20, "6": 24, "8": 32, "10": 40, "12": 48, "14": 56, "16": 64, "20": 80 },
  "layout": { "frame-width": 393, "frame-height": 852, "safe-top": 59, "safe-bottom": 34, "nav-clearance": 104, "touch-min": 44, "touch-driver": 56, "icon-grid": 24, "home-top": 71 },
  "stroke": { "hairline": 1, "focus": 1.5, "icon": 1.75, "route": 5, "route-casing": 9 },
  "size": {
    "dot-xs": 6, "dot-sm": 8, "dot-md": 10, "dot-user": 14,
    "checkbox": 22, "knob": 28, "switch-h": 32, "switch-w": 52,
    "handle-w": 36, "avatar-md": 40, "avatar-lg": 64, "control-md": 48, "input-lg": 52,
    "nav-height": 64, "quick-tile": 72, "stat-card-w": 170, "content-width": 353,
    "zoom-pill-h": 88, "hero-map-h": 548, "welcome-sheet-h": 332,
    "onboarding-sheet-h": 304, "hero-fade-h": 96, "top-scrim-h": 120, "progress-seg-w": 88,
    "auth-hero-h": 280, "auth-hero-copy-w": 280, "auth-mascot-w": 130, "auth-mascot-h": 176,
    "confirm-w": 353, "confirm-h": 56, "confirm-radius-idle": 16, "confirm-radius-circle": 28, "confirm-px": 14, "icon-xs": 16, "stroke-check": 3, "matrix-dot": 2, "matrix-gap": 2, "matrix-grid": 14,
    "bell-btn": 36, "weather-pill-h": 36, "search-pill-h": 46, "saved-chip-h": 32, "home-content-w": 361,
    "mascot-hero-w": 393, "mascot-hero-h": 160, "mascot-band-h": 84, "mascot-art-w": 132, "mascot-art-h": 150, "speech-bubble-w": 233, "speech-tail-w": 14, "speech-tail-h": 16
  }
}
```