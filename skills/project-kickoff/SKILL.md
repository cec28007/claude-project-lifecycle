---
name: project-kickoff
description: Turn a piece of work into a Claude Code project that sessions can run with little supervision. Use when asked to "kick off a project", "turn this into a project", "set up a project for this", or "should this be a project?". Vets the idea first (with the project-manager skill), then makes the repository ready for unattended work, writes a kickoff file every new session reads first, builds the project instructions from shared blocks, and draws the first project map.
---

# Project kickoff

A project works when any new session can open the repository cold and know the goal, the rules,
the next ticket, and where everything stands. This skill builds those pieces, in this order.

## 0. Vet the idea first

Use the `project-manager` skill, sections 1 and 2: route the idea and, if it is a project, write
the one-page brief. Build nothing until the owner has edited or approved the brief. The brief is
the only plan; everything below is cut from it.

## 1. Make the repository ready for unattended work

Do what is missing; skip what exists.

- **Tests and continuous integration on every pull request.** Sessions merge only on green
  checks, so the checks are the gate. No checks yet → the first ticket is to add them.
- **A `CLAUDE.md`** with a three-line pointer to the kickoff file and the project-map list.
- **Hooks** in `.claude/settings.json`: run the tests after edits; block commits to `main`.
- **A reviewer.** Every pull request gets a code review before merge.
- **Tickets.** Cut the brief's parts into tickets. Each one: goal, files, done-when.
- **The `project-map` subagent** copied into `.claude/agents/`.

## 2. Write the kickoff file

`docs/handoffs/<YYYY-MM-DD>-<slug>-project-kickoff.md` from `templates/kickoff-template.md`.
Distil, don't dump. Restate anything that lives only on the owner's computer (personal notes,
rules from other tools), because cloud sessions can't read it. Include the first 2–5 tickets.
Merge it to `main` before the project starts: a project reads the default branch, and an
unmerged pull request is invisible to it.

## 3. Build the project instructions

Instructions = a short project-specific top (what it is, where the work lives, project rules)
plus shared blocks that every project uses. Keep the blocks in `blocks/` and write `{{block-name}}`
where each goes; `build-instructions.py <file>` fills them in and checks the length (Claude Code
projects allow 16,000 characters). Starter blocks:

- `blocks/approvals.md` — what a session may do alone and what needs the owner's go.
- `blocks/reply-format.md` — how every reply is laid out, so the owner can scan many sessions.
- `blocks/project-map.md` — how and when the map is redrawn.

Edit them to fit you. When a rule changes, change the block and rebuild every project.

## 4. Draw the first map

Run the `project-map` subagent against the repository, commit `docs/project-maps/<slug>.html`
with the kickoff pull request, publish it somewhere with a fixed link if you can, add the link
to the project's "Where the work lives", and add a card to the hub (see `project-manager` §4).

## 5. Create the project yourself

Don't hand the owner a form to fill in. If a browser tool is signed in to claude.ai (Claude in
Chrome, or a built-in browser), create the project and fill every field:

1. `https://claude.ai/code/projects/browse` → "New project".
2. Name and Goal: click each field, then type.
3. Context → "+ Add" opens a repository list. Don't type a search: the keystrokes can land in the
   Name field. Find each repository by name and click its checkbox, then close the list by clicking the
   dialog's title. Don't press Escape: it closes the whole form and loses every field.
4. Zoom in on the dialog and check the Name before you create. If it is wrong: click, select all, retype.
5. Click "Create project" by element reference, not by screen position. The page moves to
   `claude.ai/code/project/<id>`; keep that id.
6. Open Project settings and paste the built instructions (Memory), set effort and auto-continue
   (General; the coordinator effort starts at Low), and the repositories, local-folder access and
   worktrees (Environment). Reload and check each value stayed.

If no browser is signed in, the only ask is "open the browser and sign in".

## 6. First message to the project

"Read docs/handoffs/<file>.md and docs/project-maps/<slug>.html, then propose sessions for the
tickets and start the first one."

Send it yourself, in the browser: wait for the project page to finish loading, click the prompt box,
type, and zoom to check the text is in the box before pressing Enter. Typing sent while the page is
still loading is dropped without an error.

## Traps

- Cloud sessions can't see your local skills, subagents, or notes. Put what matters in the
  repository (`.claude/skills`, `.claude/agents`, the kickoff file, the instructions).
- Instruction changes reach new sessions only.
- Publish the map before you create the project, so its link goes into the instructions in one pass.
- No secrets in the instructions, the kickoff file, or the map.
