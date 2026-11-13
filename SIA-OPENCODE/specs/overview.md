# Project Overview

**Product name:** Loc8 (logo TBD)
**Related spec:** `DESIGN.md` (design system)

## 1. Summary

Loc8 is a mobile application for **commuters** and **jeepney drivers**. Drivers share their live location during a trip. Commuters see approaching jeepneys on a map, with arrival estimates and alerts at their chosen waiting point. Drivers get a passenger-demand view (hotspots) showing where passengers are likely waiting.

A **jeepney cooperative (coop)** acts as the admin: it registers and verifies drivers and jeepneys, assigns drivers, and sets fares. The coop dashboard (with LTFRB and LTO roles) comes in a later stage and is not part of the current design work.

## 2. Goals

1. Reduce commuter waiting uncertainty: where to wait, which jeepney is coming, when it arrives.
2. Help drivers see where passenger demand is along their route.
3. Keep both experiences simple, visual, and easy to understand at a glance.

## 3. Users

| Role | Description |
|---|---|
| **Commuter** (primary user) | Finds jeepneys, waits at a point, gets alerts, tracks arrival. |
| **Driver** | Shares live location, sets seat status, views hotspots. Cannot sign up. The coop creates the account. |

**Current design scope:** commuter app and driver app, in one mobile app with role-based screens.

## 4. Accounts and entry flow

| Item | Commuter | Driver |
|---|---|---|
| Sign up | First name, last name, birthdate, email **or** phone, password | None. The coop creates the account. |
| Login | Email or phone + password, Google, Facebook | Coop-registered email or phone, Google, Facebook |
| OTP | Login and sign up | Login |

**Shared screens:** Get Started (3 slides), Privacy Policy, Terms and Conditions, Login, OTP.

```
Splash → Get Started (3 slides) → Choose role (Commuter / Driver)
  → Login (or Sign up, commuter only) → OTP
  → Privacy Policy + Terms (first time) → Home
```

## 5. Commuter app

Bottom navigation: **Home · Map · Activity · Profile**, with a center **Waiting** button.

- **Home:** greeting header (date, greeting, weather, notifications), **Loc8 mascot hero** with a short message, nearest-jeepney card (route, seats left, ETA), active-waiting banner, find-a-jeepney card, service alerts, fare card (Regular and Senior/PWD), recent routes. No search bar and no saved places on Home — search and saved places live on **Map**.
- **Map:** live jeepneys, routes, stops and waiting points, layer toggles, tap-to-view details, recenter button, stale-location indicator.
- **Waiting flow:** choose route and waiting point, start waiting, ETA ring, alert settings, "I boarded", then rating.
- **Activity:** current waiting or ride, trip history.
- **Profile:** passenger type (Regular, Senior, PWD), saved places and routes, settings, language, privacy, help, about, log out.

## 6. Driver app

Bottom navigation: **Home · Map · [Start/End Trip] · Hotspots · Account**.

- **Home:** logo header (no driver name), status (Off duty / On trip), jeepney hero visual, readiness card, today's summary, weather, demand preview, **Start Trip** button, quick controls (Seats, Count, Fare, SOS).
- **Trip mode:** GPS status, seat status (Available / Few seats / Full), passenger counter, next stop and waiting count, pause, hold-to-confirm End Trip, trip summary.
- **Map:** assigned route, stops, waiting counts at stops, other jeepneys on the route, off-route warning.
- **Hotspots:** Now | Soon toggle, heatmap, top 3 hotspots with a flame scale.
- **Account:** profile, jeepney and documents (read-only, managed by the coop), trip history, settings, tracking help, help, about, log out.
- **Safety:** manual input locks while the jeepney is moving. Only seat status, SOS and the GPS chip stay active.

## 7. Smart features (shown to users)

- **ETA prediction:** estimated arrival time for each approaching jeepney.
- **Smart waiting-point tip:** a suggested waiting point when it will get the commuter a jeepney sooner.
- **Demand hotspots:** observed and forecast passenger demand for drivers.
- **Honest status:** every live value shows how fresh it is, and stale locations are clearly marked.

## 8. Design direction

- Font: **Plus Jakarta Sans**. White background. Black primary button.
- Soft minimalist style: pastel cards, pill buttons, floating dark nav pill, minimal text, visual-first layouts.
- One filled black button per screen.
- Full tokens, components and rules are in `DESIGN.md`.
