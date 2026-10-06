# Project lifecycle for Claude Code

**From idea to done: vet it, plan it, set it up, track it.**

Built for **Claude Code Projects**: a project is one long-running effort, like a platform or a
product, with many sessions working in it over weeks. After a few weeks, it gets hard for anyone,
person or Claude, to say where things stand. This plugin makes each project its own project
manager. Every new request goes through four steps, and the project keeps its own status current:

1. **Vet the request.** Is this a project, one session, a scheduled routine, or not ready yet? Five quick tests decide, and Claude says why in one line.
2. **Plan it.** A one-page brief: goal, finish line, parts, milestones, risks, and the few decisions only you can make. You edit it; it becomes the only plan.
3. **Set it up.** Get the repository ready for unattended work (tests on every pull request, a reviewer, tickets), write a kickoff file every new session reads first, and build the project instructions from shared blocks.
4. **Track it.** One live map per project, with status cards and a timeline (Gantt) view, redrawn after every merged pull request. One hub page links every map.

See [`examples/recipe-box.html`](examples/recipe-box.html) for a sample map (made-up project). Open it in a browser and use the Cards / Timeline toggle.

## What's inside

| Piece | Steps | What it does |
|---|---|---|
| `skills/project-kickoff` | 1–3 | Vets the idea, writes the brief, readies the repository, writes the kickoff file, draws the first map |
| `skills/project-manager` | 1, 2, 4 | Vets new work inside running projects, keeps maps current, keeps the hub page, runs a daily refresh |
| `agents/project-map` | 4 | A helper agent that draws or redraws one project's map. Reads the plan, tickets, git history and pull requests; writes only the map |

## Install

As a plugin, in Claude Code:

```
/plugin marketplace add cec28007/claude-project-lifecycle
/plugin install project-lifecycle@claude-project-lifecycle
```

Or copy by hand: put the two folders under `skills/` into `~/.claude/skills/`, and `agents/project-map.md` into `~/.claude/agents/`.

**Cloud sessions:** they only see skills and helper agents that live in the repository. For a project that runs in the cloud, also copy `agents/project-map.md` into that repository's `.claude/agents/`.

## Use it

- "Should this be a project?" → vets the idea and, if yes, writes the brief.
- "Kick off a project for this" → vets, plans, sets up the repository, draws the first map.
- "Where are we?" → redraws the map and answers from it.
- Scheduled daily refresh → redraws every map and the hub. See section 5 of `skills/project-manager/SKILL.md`.

## Design rules it follows

- Vet before building. Nothing gets set up until the brief is approved.
- Never invents dates. A part gets a bar on the timeline only from real commits, pull requests, or a target date you set.
- Risky actions (production releases, changes to shared data, sending messages, deleting) always show "needs the owner's go" and never happen by default.
- Plain English. One page per map. Readable on a phone. No external scripts.

## Credit

Inspired by [this post from Vox (@Voxyz_ai)](https://x.com/Voxyz_ai/status/2107455844992299272) about giving AI coding projects a visible map.

## License

MIT
