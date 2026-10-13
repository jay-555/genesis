# Knowledge Management System

## Why this structure exists

You asked to track five things clearly:

1. Daily code changes and implementation logs  
2. Notes and learnings  
3. Questions and answers  
4. Architecture and flow diagrams  
5. Reference documents  

Plus a **Revision Notes** hub that consolidates the important bits for quick review.

## Folder map

```
genesis/
├── ROADMAP.md / PROGRESS.md / README.md
├── 00-meta/          how the system works + templates
├── 01-daily/         primary working area (week/day)
├── 02-notes/         polished topic notes by section
├── 03-qa/            reusable Q&A banks
├── 04-diagrams/      architecture / flows / whiteboards
├── 05-references/    papers, cheatsheets, link lists
├── 06-projects/      P0–P12 project workspaces
├── 07-assessments/   tests, mock interviews, system design
└── 08-revision/      consolidated revision (single place)
```

## Daily workflow (10 minutes of logging)

For every learning day:

1. Copy templates from `00-meta/templates/` into `01-daily/week-XX/day-YY/` if the day folder is empty.
2. Fill:
   - `notes.md` — concepts, analogies, key takeaways
   - `qa.md` — mentor questions + your answers + corrections
   - `code-log.md` — what you coded, errors, fixes, decisions
   - `code/` — runnable scripts for that day
   - `diagrams/` — Mermaid / Excalidraw exports for that day (optional)
3. After the day is solid, promote durable content:
   - Key concept → `02-notes/section-*/`
   - Strong Q&A → `03-qa/`
   - Reusable diagram → `04-diagrams/`
   - Paper / link → `05-references/`
4. Update **Revision Notes**:
   - `08-revision/by-week/week-XX.md`
   - Section summary when the section ends → `08-revision/by-section/`
   - Mistakes → `08-revision/mistakes-log/`
   - Architecture decisions → `08-revision/decisions/`
5. Update `PROGRESS.md` (status, scores, revision queue).

## Naming conventions

| Item | Pattern | Example |
|---|---|---|
| Week folder | `week-01` … `week-30` | `01-daily/week-01/` |
| Day folder | `day-01` … `day-06` | `day-01/` (Sat = day-06) |
| Project | `pNN-short-name` | `06-projects/p00-text-analyzer/` |
| Diagram | `YYYY-MM-DD-topic.mmd` or `.png` | `2026-10-12-ai-family-tree.mmd` |
| Weekly test | `wXX-test.md` | `07-assessments/weekly-tests/w01-test.md` |
| Mock interview | `mi-NN.md` | `07-assessments/mock-interviews/mi-01.md` |

## What goes where (decision guide)

| Content | Put it in |
|---|---|
| Today's learning + homework answers | `01-daily/...` |
| Something you want to remember long-term | `02-notes/` + promote to `08-revision/` |
| Interview-style Q you might see again | `03-qa/interview-bank/` |
| Architecture / data flow | `04-diagrams/` + link from revision |
| PDF, paper, official doc link | `05-references/` |
| Multi-day build | `06-projects/` |
| Graded work | `07-assessments/` |
| "I need to revise this before the test" | `08-revision/` |

## Revision Notes rules

`08-revision/` is the **only place** you should open the night before a weekly test or mock interview.

It must contain, per week/section:

- Key definitions (1–2 lines each)
- Must-remember diagrams (or links)
- Corrected Q&A (your wrong answers + ideal answers)
- Code snippets worth memorizing
- Decisions (why X over Y)
- Mistakes / weak areas
- Link back to the daily folder for full detail

Do **not** dump everything into revision. Compress: prefer bullets over essays.

## Mentor interaction rule

When chatting with your mentor:

- Answer daily check questions → save into that day's `qa.md`
- After feedback, update `08-revision/by-week/week-XX.md`
- Say *"continue Week X Day Y"* and the mentor will use this folder tree
