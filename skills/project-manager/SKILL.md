---
name: project-manager
description: Project management for a Claude Code project or long-running repo — vet new work (project, one session, scheduled routine, or not yet), write a one-page brief, keep each project's progress map current, and keep one hub page that links every map. Use when asked "where are we?", "should this be a project?", "vet this idea", "plan this", "update the map", after a pull request merges, or from a scheduled daily refresh.
---

# Project manager

One person can run several projects with Claude only if they can see, in seconds, where each
one stands. This skill keeps three things true: new work is vetted before it starts, every
project has one map, and one hub page links all the maps.

## Setup (once per project)

1. Copy the `project-map` subagent (`agents/project-map.md` in this package) into the repository's `.claude/agents/`. Cloud sessions only see
   subagents that live in the repository.
2. Add a short "Project maps" list to the repository's `CLAUDE.md`: each project's name, its map
   file (`docs/project-maps/<slug>.html`), and where the published map lives (a link, if any).
   This skill reads that list; it holds no links of its own.

## 1. Vet new work

Score five tests: clear finish line; more than one sitting; two or more parts can run side by
side; the owner will want to check in later; one or two repositories. Work that needs the owner's
own computer or browser counts against, because only one session can drive it at a time. Pick one
route and say why in a line:

- **Project** (4–5 yes): write a brief.
- **One session** (3 or fewer, or one sitting does it): say so and stop.
- **Scheduled routine**: the same steps repeat on a calendar.
- **Not yet**: no finish line can be written. Name the missing fact.

New work inside an existing project gets the same test: a new milestone, or a new thread?

## 2. The brief (one page, the owner edits it)

Write `docs/briefs/<YYYY-MM-DD>-<slug>-brief.md` from `templates/brief-template.md` (in this skill folder) with:
Route and score · Goal (2–4 sentences) · Finish line (an observable check) · Parts (one line
each, "done when …") · Milestones (parts and target date, or "none"; never guess a date) · Risks
(with the early sign) · Only the owner can decide (money, people, business meaning; each with a
recommendation) · Out of scope.

After the owner's OK the brief is the only plan: its parts become tickets and map cards, its
milestones the map's milestones, its "Only the owner" items the map's "Waiting on the owner".

## 3. Keep the map current

Redraw with the `project-map` subagent after every merged pull request, before any long
unattended run, and when asked "where are we?". Commit the file in the same pull request. If you
can publish (for example a claude.ai Artifact, a docs site, or an internal web page), republish
the file to its fixed link, then update that project's card on the hub.

Gated items (production releases, writes to shared data, sending messages, deleting, account
settings) always show "needs the owner's go" and never go ahead by default.

## 4. The hub (one page for all projects)

Start from `templates/hub.html` (in this skill folder). One card per project with: next milestone and how many steps
are left, the next step, what waits on the owner, and links to the map and its `#timeline`.
Put "Drawn <date>" in the subtitle. Publish it to one fixed link that never changes, so the owner
can bookmark it.

## 5. Daily refresh (for a scheduled routine)

For each map in the "Project maps" list: run the `project-map` subagent in that map's repository,
writing to its file. Do not commit or push. Republish each file to its link. Then rebuild the hub
from each map's top strip and republish it. End with one line per project: what changed since the
last run, or "no change". Never invent dates; never mark a gated item as done.
