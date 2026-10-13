# Week 01 · Day 02 — Code / Implementation Log

**Date:** 2026-10-13  
**Topic:** Python string drills  
**Environment:** `.venv` · Windows

---

## Goal
Practice variables, strings, methods, and f-strings used constantly in GenAI work.

## Changes made
| Time | File | Change | Why |
|---|---|---|---|
| Day 2 | `code/day2_string_drills.py` | Ran drills | Hands-on practice |

## Commands run
```powershell
cd "D:\Work\AI Learning\genesis"
.\.venv\Scripts\Activate.ps1
python .\01-daily\week-01\day-02\code\day2_string_drills.py
```

## Bugs / errors faced
| Error | Cause | Fix |
|---|---|---|
| Expected unique=1, got 2 | Trailing `.` on some prompts | Learned: strip+lower ≠ full normalize; remove punctuation too |

## Result
- [x] Script runs
- [x] Output logged in `qa.md` (unique count 2 — explained)
- [x] Answers filled in `qa.md`

## Snippet worth keeping
```python
normalized = [p.strip().lower() for p in prompts]
# Still may differ by punctuation: "pdf." vs "pdf"
```

## Next steps
- Day 2 closed → Day 3 (lists, dicts, loops, word-frequency)
