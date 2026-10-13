# Week 01 · Day 01 — Code / Implementation Log

**Date:** 2026-10-12  
**Topic:** Toy next-word language model + environment setup  
**Environment:** Python (system) · venv: `.venv` · OS: Windows 10

---

## Goal
1. Create and activate a project virtual environment
2. Run a tiny next-token (next-word) generator to feel how LLMs generate text

## Changes made
| Time | File | Change | Why |
|---|---|---|---|
| Day 1 | `code/day1_next_word.py` | Added toy language model | Demonstrate next-token prediction |
| Day 1 | repo root `.venv/` | Created virtualenv | Isolate course dependencies |

## Commands run
```powershell
cd "D:\Work\AI Learning\genesis"
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python .\01-daily\week-01\day-01\code\day1_next_word.py
```

## Bugs / errors faced
| Error | Cause | Fix |
|---|---|---|
| `Activate.ps1` blocked (possible) | Execution policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |

## Decisions
| Decision | Options considered | Chose | Why |
|---|---|---|---|
| Where to put day code | flat `week01/` vs knowledge tree | `01-daily/week-01/day-01/code/` | Matches knowledge system |
| Toy model unit | characters vs words | words | Clearer for Day 1 intuition |

## Result
- [x] Runs successfully (2026-10-13)
- [x] Output varies across `generate("i")` calls (5 different generations logged in `qa.md` Q7)
- [x] Environment activated with `(.venv)` prefix

## Sample output (learner)
```
1. i love machine learning . i love machine learning
2. i love generative ai creates new text . i
3. i love generative ai creates new text . generative
4. i love machine learning learns from data . generative
5. i love generative ai creates new text . generative
```

## Snippet worth keeping (for revision)
```python
next_words = defaultdict(Counter)
for current, nxt in zip(words, words[1:]):
    next_words[current][nxt] += 1
# generation = sample from next_words[last]
```

## Next steps
- Day 1 closed — proceed to Day 2 (Python strings & basics)
