# Week 01 · Day 02 — Q&A

**Date:** 2026-10-13  
**Topic:** Python strings & basics  
**Status:** Completed  
**Day score:** 5 / 5 Correct · **Gate:** Pass → Day 3

---

## Understanding check

### Q1
**Question:** What is the difference between `'hello'` and `"hello"` in Python?  
**My answer:** There is not basic difference, For both python will consider there type as str.

**Correct / Ideal answer:**  
No difference in value or type — both are `str`. The only practical difference is which quote is easier when the string itself contains quotes (e.g. `"It's fine"` vs `'say "hi"'`).

**Status:** Correct  
**What I learned:** Single and double quotes are interchangeable for normal strings.

### Q2
**Question:** What does `s[0]`, `s[-1]`, and `s[1:4]` return for `s = "Generative"`?  
**My answer:** `s[0] = 'G'; s[-1] = 'e'; s[1:4] = 'ene'`

**Correct / Ideal answer:**  
`'G'`, `'e'`, `'ene'`. Slice end index is **exclusive** — `s[1:4]` takes indices 1,2,3. For `"ener"` use `s[1:5]`.

**Status:** Correct  
**What I learned:** Indexing from 0; `-1` is last; slice `[start:end)` excludes end.

### Q3
**Question:** Write an f-string that prints: `Model GPT costs $0.03` using variables `name="GPT"` and `price=0.03`.  
**My answer:** `f'Model {name} costs ${price}'`

**Correct / Ideal answer:**  
`f"Model {name} costs ${price}"` (or the same with single quotes — both fine).

**Status:** Correct  
**What I learned:** Put expressions inside `{...}` in an f-string.

### Q4
**Question:** Why might we `.lower()` and `.strip()` text before comparing user input or training NLP models?  
**My answer:** while comparing we don't want the entry of same word twice only due to there case difference and blank space. To create uniformity.

**Correct / Ideal answer:**  
Normalize case and whitespace so `" Hello "` and `"HELLO"` count as the same text — critical for deduping prompts, matching intents, and cleaner NLP features.

**Status:** Correct  
**What I learned:** Cleaning = uniformity before compare / train / embed.

### Q5 (practical)
**Question:** Paste the output of `day2_string_drills.py` after you complete the TODOs.  
**My answer:**  
```
TYPES
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>

INDEX / SLICE
first: G
last: e
slice 1:4: ene
ener?: ener

METHODS
cleaned: 'hello genai world!'
words: ['hello', 'genai', 'world!']
joined: hello-genai-world!
replace: hello generative-ai world!
startswith hello?: True

F-STRING
Model GPT costs $0.03

PROMPT NORMALIZE
normalized: ['summarize this pdf.', 'summarize this pdf.', 'summarize this pdf']
unique count: 2

YOUR TURN
sentence: Large language models predict the next token.
words: 7
chars (no spaces): 39
```

**Correct / Ideal answer:**  
Script runs successfully. Bonus insight: unique count is **2**, not 1, because the third prompt has **no period**. `strip()` + `lower()` do not remove punctuation.

**Status:** Correct (+ strong observation)  
**What I learned:** Text normalization often also needs punctuation cleanup (e.g. remove `.?!`) for true duplicates — preview of NLP cleaning in Week 5.

---

## Profile reminder
Python: basic · ML: a little · Prefer English videos
