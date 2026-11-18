# CLAUDE.md

## Project
Figma-first design repo. There is no application code (no package.json, no build, test or lint). Do not scaffold an app or run npm commands unless the user explicitly asks for code.

@DESIGN.md
@specs/overview.md

- `specs/overview.md` is the single source of truth for **what the system does**: users, features, flows, routes, rules.
- `DESIGN.md` is the single source of truth for **how it looks**: tokens, layout, components, motion. Add a token there before using a new value. Long per-component specs live in `design/*.md`, linked from `DESIGN.md` section 11.
- This file holds only instructions on how to work. It holds no project or design content.

## Keeping the docs up to date
Requirements and design change often. When the user discusses a change, decide where it belongs, then update that file.

| The change is about... | Update |
|---|---|
| Users, roles, features, screens' purpose, flows, routes, data rules, privacy, scope | `specs/overview.md` |
| Colors, type, spacing, radius, components, layout, motion, visual rules | `DESIGN.md` |
| Both (for example, a new feature that needs a new component) | Both. Put the behavior in `overview.md` and the look in `DESIGN.md`. Never repeat the same content in both files. |
| How Claude should work (this file's rules) | `CLAUDE.md`, only when the user asks |

Rules:
1. **Update on decisions, not on ideas.** Brainstorming, options and questions do not change the docs. Update when the user decides ("let's do X", "remove Y", "change Z to ..."). If it is unclear whether something is decided, ask.
2. **Edit the existing text.** Change or remove the old line. Do not add a note next to it, and do not leave the old version behind. Remove anything that is now unused (tokens, components, features).
3. **Fix every place the change touches.** Check both files, `DESIGN.md` section 11 (component registry) and any linked `design/*.md` file for mentions of the thing you changed, so the files never contradict each other.
4. **Keep each file in its lane.** No visual details in `overview.md`. No feature or business rules in `DESIGN.md`. If a rule about the system shows up in `DESIGN.md`, move it to `overview.md`.
5. **If the two files conflict, stop and ask** the user which is correct. Do not pick one silently.
6. **Tell the user what changed.** After editing, give a short list: file, section, what changed. For a big or risky change (removing a feature, changing a token used in many places), say what it affects and ask before editing.
7. **Figma follows the docs.** If a doc change means the Figma file is out of date, say so and list what needs updating. Do not change Figma unless asked.

## Figma
- File key: `JAryzeTw3PfSgV8mvozSf6` (https://www.figma.com/design/JAryzeTw3PfSgV8mvozSf6/Transpo-App). If the user gives another frame URL, use theirs.
- Start with `create_session` using the file key, then `get_metadata` to see the pages and frames.
- Load `/figma-use` before any `use_figma` call.
- This is design work only. Do not generate code from designs.
- Existing frames may hold placeholder content. Build to the spec, not to what is on the canvas.
- Screenshots: take one at a time with `maxDimension` 500 or less. If a screenshot does not return, skip it and tell the user to check visually.

## Reuse before create
- Before building any element, look for an existing one in this order:
  1. Components on the Foundations page of this file. List them with `get_metadata`, and also try `search_design_system`.
  2. The component registry in `DESIGN.md`
- If a match exists, use an instance of it. Do not redraw or restyle it.
- Never create a new component, icon or illustration unless the user says "create a new component/asset".
- If nothing fits and the user did not ask for a new one, stop and ask.
- Allowed changes: text, state, size variant, token-bound fill. Not allowed: structure, radius, shape or icon style.
- When you finish, list the components you reused and any you created (created should be zero unless requested).

## Working style
- Keep responses concise unless asked otherwise.
- Plan first and ask clarifying questions. Do not assume stack, design or features. Never invent missing information. Stop and ask.
- Delegate to sub-agents where it helps, and run independent work in parallel.
- Report which checks you ran and what they showed.
