# Decision: Knowledge system folder layout

**Date:** 2026-10-13 · **Week:** 1 · **Project:** workspace meta

## Context
Need a clear place for daily logs, notes, Q&A, diagrams, references, and a consolidated revision area.

## Options considered
| Option | Pros | Cons |
|---|---|---|
| Flat folders (`Daily Notes`, `Q&A`) | Simple | Hard to find week/day; no revision hub |
| Week/day tree + typed top-level folders | Clear paths; scales to 30 weeks | Slightly more structure |
| Everything only in Obsidian-style daily notes | Flexible | Weak project/code separation |

## Decision
Use numbered top-level folders `00`–`08` with `01-daily/week-XX/day-YY/` as the primary working area and `08-revision/` as the single revision hub.

## Why
- Matches the 30-week roadmap
- Separates ephemeral daily work from durable revision
- Keeps code, diagrams, assessments, and projects discoverable

## Revisit when
If daily logging feels heavy after Week 2 — simplify templates, not the folder map.
