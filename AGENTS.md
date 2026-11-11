# AGENTS.md

## What this repo is

A Figma-first design repo for a jeepney tracking app (Commuter + Driver roles). There is **no application code**: no `package.json`, no build/test/lint, and it is not a git repo. Do not scaffold a Next.js app or run `npm`/`next` commands unless the user explicitly asks for code.

## Read first

- `DESIGN.md` — design system and single source of truth for every token (color, type, spacing, radius, shadows) plus component specs. Add a token here before using a new value.
- `specs/overview.md` — product scope, roles, screen list, and feature intent.


## Figma is the deliverable

- File: https://www.figma.com/design/JAryzeTw3PfSgV8mvozSf6/Transpo-App?node-id=135-169 (file key `JAryzeTw3PfSgV8mvozSf6`). If the user supplies another frame URL, use theirs.
- Pages: `0:1` Foundations (tokens + components), `3:2` Login-Signup-OTP-Terms-Privacy, `3:3` Commuter, `3:4` Driver, `3:5` Admin.
- Screen frames are named `Commuter / 0N <Screen>` and `Driver / 0N <Screen>` at `393 x 852`; inner screens may still hold placeholder content, so build to the spec rather than copying what is there.
- MCP flow: `create_session` with the file key first, then `get_metadata` for structure, `get_design_context` only when turning a design into code. Load `/figma-use` before any `use_figma` call.
- Reuse Foundations components (`Badge/Route`, `Chip/GPS`, `IconCircle/Tint`, `Floating Commuter Nav`, `Button/Primary/...`) via `search_design_system` before creating new ones.
- Screenshots: one at a time, `maxDimension` 500 or less. If a screenshot does not return, skip it and tell the user to check visually.

## Rules that are easy to break

- Never hard-code hex values, font sizes, radii, or spacing; bind to the tokens in `DESIGN.md`.
- One filled black button per view. `accent` blue is for live/go/location only, not actions.
- At most 3 to 4 cards above the fold. One tint per card, max 3 tints per screen; tinted cards get no shadow and no border.
- Seat counts cannot be inferred from GPS: show driver-entered counts or a state (`Likely free` / `Almost full` / `Unknown`) with an "updated N min ago" line. Never imply exact free seats from location data.
- Respect `layout/safe-top` 59, `layout/safe-bottom` 34, 20 px side padding, and 104 px bottom clearance for the floating nav.

## Reuse before create (hard rule)

- Before building ANY element, search for an existing one in this order:
  1. Foundations components in Figma (`search_design_system`)
  2. The Component registry in `DESIGN.md` section 12
- If a match exists, use an instance of it. Do not redraw, restyle, or "improve" it.
- Never create a new component, icon, or illustration unless the user explicitly says
  "create a new component/asset". That request is the ONLY permission to create one.
- If nothing fits and the user did not ask for a new one, STOP and ask. Do not improvise.
- Variants and overrides allowed: text, state, size variant, token-bound fill. Not allowed: changing structure, radius, shape, or icon style.
- When you finish, list which existing components you reused and any you created (created ones should be zero unless requested).

## Working style (user preferences)
- Keep responses concise unless asked otherwise.
- Plan first: ask clarifying questions; do not assume stack, design, or features. Never invent missing information — stop and ask.
- Delegate implementation to sub-agents and act as coordinator; parallelize independent work.
- Report which checks ran and their results. If app code is later added, run its lint, typecheck, and build before claiming a task is done.
