# Project Overview

**Product name:** Loc8 (logo TBD)
**Project title:** An Interactive GPS-Driven Mobile Application for Real-Time Jeepney Detection and Proximity Alerts along the Bugasong to San Jose Route
**Related spec:** `DESIGN.md` (all visual design, layout, components and motion)

> **Scope of this file:** what the system does, who uses it, and the rules it follows. It does not define how anything looks. For colors, typography, layout, components, navigation styling and motion, read `DESIGN.md`. If this file and `DESIGN.md` disagree on anything visual, `DESIGN.md` wins.

## 1. Summary

Loc8 is a mobile application for **commuters** and **jeepney drivers**. Drivers share their live location during a trip. Commuters see approaching jeepneys on a map, with arrival estimates and alerts at their chosen waiting point. Drivers get a passenger-demand view (hotspots) showing where passengers are likely waiting.

A **jeepney cooperative (coop)** acts as the admin: it registers and verifies drivers and jeepneys, assigns drivers, and sets fares. The coop dashboard (with LTFRB and LTO roles) comes in a later stage and is not part of the current scope.

## 2. Goals

1. Reduce commuter waiting uncertainty: where to wait, which jeepney is coming, when it arrives.
2. Help drivers see where passenger demand is along their route.
3. Keep both experiences simple, and keep driver interaction minimal and safe while the jeepney is moving.

## 3. Users

| Role | Description |
|---|---|
| **Commuter** (primary user) | Finds jeepneys, waits at a point, gets alerts, tracks arrival. |
| **Driver** | Shares live location, sets seat status, views hotspots. Cannot sign up. The coop creates the account. |
| **Coop admin** (later stage) | Registers and verifies drivers and jeepneys, assigns drivers, sets fares. Not in the current scope. |

**Current scope:** commuter app and driver app, in one mobile app with role-based screens.

## 4. Routes

The system supports exactly **3 routes**:

| Code | Route |
|---|---|
| R1 | Bugasong |
| R2 | San Jose |
| R3 | Patnongon |

No other routes are supported in the current scope.

## 5. Accounts and entry flow

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

## 6. Commuter app

Navigation: **Home · Map · History · Profile**, plus a **+** action button. Tapping + opens a small menu with two choices: **Chat** and **Start waiting**. Each opens as its own full-screen page with a back button.

- **Home:** date, greeting, weather and notifications; while the commuter is waiting, an active waiting card right below the mascot hero and before the other cards, showing the jeepney being waited for, the From → To stops, the ETA countdown (under 1 minute shows "Arriving"), how fresh its location is, and an "I boarded" action; tapping the card opens the waiting details, and the card is hidden when the commuter is not waiting; nearest-jeepney info (route, seats left, ETA); service alerts; fares: pick the boarding municipality to see the fare to each other municipality, and drag a municipality's bar to a shorter distance (1 km up to the full trip) to see the fare for getting off earlier; Regular and Student/Senior/PWD (20% off, rounded to the nearest 25 centavos), with the computation shown (base fare for the first 4 km, ₱2.00 per extra km, discount, rounding), from the LTFRB PUJ fare guide effective Sept 28, 2026. Road distances between municipalities are placeholders until real km are provided. Search and saved places are not on Home. They live on **Map**.
- **Map:** live jeepneys, routes, stops and waiting points, layer toggles, tap-to-view details, recenter, stale-location indicator, search, saved places.
- **Waiting flow:** tap + then Start waiting, pick a route (Bugasong, San Jose or Patnongon) and see its stops and the live jeepneys near each stop, first pick the stop they are waiting at (From), then their destination stop (To); each can be any stop on any of the 3 routes, so a trip can cross municipalities; see the estimated fare for that trip (Regular or Student/Senior/PWD, same fare rules as the Home fares; stop and municipality distances are placeholders until real km are provided), start waiting (a short toast confirms it and the waiting card appears on Home; the Start waiting page always opens empty, never with an earlier pick), ETA countdown, alert settings, "I boarded", then rating.
- **Chat:** ask Loc8 (the mascot) questions in plain language about arrival times, fares, routes and stops. Chat only answers questions; it cannot start waiting, book or change anything. Answers follow the same data rules as the rest of the app (freshness shown, seat counts are driver-entered). A note under the input says answers can be wrong. Replies in the prototype are placeholders until the assistant is built.
- **History:** trip history grouped by day (Today, Yesterday, then dates), with the Loc8 mascot at the top saying how many rides the commuter took this week (the average wait is not shown); each trip can be rebooked, reported, or opened for details. A filter narrows the list by time period (this week, last 30 days, all time; one at a time) and by route (any mix of R1, R2, R3), shows how many trips match, and can be reset. Rebook opens a short confirmation with the last fare and jeepney, then shows the live jeepneys on that route. Trip details shows the route, fare, status (for example Completed), date, time, jeepney, wait time and fare, with Report issue and Rebook. Report issue shows the trip, asks what went wrong (Overcharged fare, Long wait, Unsafe driving, Wrong route, Other; one choice) with optional details, then submits the report. When there are no trips, an empty state offers Start waiting. The current wait is not on this page; it lives on Home.
- **Profile:** the commuter's name, email and passenger type (Regular, Student, Senior or PWD), with Edit; preferences: arrival alerts (notify 2 min before arrival), live location (shared only as an anonymous stop-wait count) and language; help and support: how Senior or PWD discounts work, how free seats and ETAs are updated, report a problem (route, fare or GPS issue), email the cooperative; about: Terms and Conditions, Privacy Policy; log out; app version. Saved places live on **Map**, not on Profile.

## 7. Driver app

Navigation: **Home · Map · Start/End Trip · Hotspots · Account**.

- **Home:** driver status (Off duty / On trip), readiness check, today's summary, weather, demand preview, **Start Trip**, quick controls (Seats, Count, Fare, SOS). The driver's name is not shown.
- **Trip mode:** GPS status, seat status (Available / Few seats / Full), passenger counter, next stop and waiting count, pause, hold-to-confirm End Trip, trip summary.
- **Map:** assigned route, stops, waiting counts at stops, other jeepneys on the route, off-route warning.
- **Hotspots:** current and forecast demand, with the top 3 hotspots ranked by demand level.
- **Account:** profile, jeepney and documents (read-only, managed by the coop), trip history, settings, tracking help, help, about, log out.
- **Safety:** manual input locks while the jeepney is moving. Only seat status, SOS and the GPS status stay active.

## 8. Smart features

- **ETA prediction:** estimated arrival time for each approaching jeepney. An ETA under 1 minute is shown as "Arriving".
- **Smart waiting-point tip:** a suggested waiting point when it will get the commuter a jeepney sooner.
- **Demand hotspots:** observed and forecast passenger demand for drivers.
- **Honest status:** every live value shows how fresh it is, and stale locations are clearly marked as stale or offline.

## 9. Data and privacy rules

- **Seat counts are driver-entered.** The app shows the driver's last entry (capped at 20 seats). It never infers seat availability from GPS.
- **GPS status levels:** live, weak or delayed, lost, stale. Every live value carries a freshness time.
- **Commuter privacy:** drivers and the coop only see aggregate counts (for example, waiting counts at stops and demand levels). Exact commuter locations and individual commuter identities are never shown.
- **Driver accounts** are created only by the coop. Drivers cannot self-register.
- **Documents** shown in the driver Account are read-only and managed by the coop.

## 10. Out of scope (for now)

- Coop / LTFRB / LTO web dashboard.
- Any route other than R1, R2 and R3.
- Driver self sign-up.
