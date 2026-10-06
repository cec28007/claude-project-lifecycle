# Project manager for Claude Code

Run several Claude Code projects at once and still see, in seconds, where each one stands.

This plugin gives Claude three habits:

1. **Vet new work before it starts.** Is this a project, one session, a scheduled routine, or not ready yet? Five quick tests decide.
2. **Write a one-page brief.** Goal, finish line, parts, milestones, risks, and the few decisions only you can make. You edit it; it becomes the only plan.
3. **Keep a live map of every project.** One HTML page per project with status cards and a timeline (Gantt) view, redrawn after every merged pull request. One hub page links them all.

See [`examples/recipe-box.html`](examples/recipe-box.html) for a sample map (made-up project). Open it in a browser and use the Cards / Timeline toggle.

## What's inside

| Piece | What it does |
|---|---|
| `skills/project-manager` | Vetting, briefs, keeping maps current, the hub page, a daily refresh routine |
| `skills/project-kickoff` | Turns a brief into a project sessions can run with little supervision: repo readiness, a kickoff file, shared instruction blocks, the first map |
| `agents/project-map` | A subagent that draws or redraws one project's map. Reads the plan, tickets, git history and pull requests; writes only the map |

## Install

As a plugin, in Claude Code:

```
/plugin marketplace add cec28007/claude-project-manager
/plugin install project-manager@claude-project-manager
```

Or copy by hand: put the two folders under `skills/` into `~/.claude/skills/`, and `agents/project-map.md` into `~/.claude/agents/`.

**Cloud sessions:** they only see skills and subagents that live in the repository. For a project that runs in the cloud, also copy `agents/project-map.md` into that repository's `.claude/agents/`.

## Use it

- "Should this be a project?" → vets the idea and, if yes, writes the brief.
- "Kick off a project for this" → vets, briefs, readies the repo, writes the kickoff file, draws the first map.
- "Where are we?" → redraws the map and answers from it.
- Scheduled daily refresh → redraws every map and the hub. See section 5 of `skills/project-manager/SKILL.md`.

## Design rules it follows

- Never invents dates. A part gets a bar on the timeline only from real commits, pull requests, or a target date you set.
- Risky actions (production releases, changes to shared data, sending messages, deleting) always show "needs the owner's go" and never happen by default.
- Plain English. One page per map. Readable on a phone. No external scripts.

## Credit

Inspired by [this post from Vox (@Voxyz_ai)](https://x.com/Voxyz_ai/status/2107455844992299272) about giving AI coding projects a visible map.

## License

MIT
