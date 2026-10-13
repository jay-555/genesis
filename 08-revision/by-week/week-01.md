# Revision — Week 01

**Section:** A — Foundations  
**Status:** In Progress (Day 1–2 ✅ · Day 3 open)  
**Weekly test score:** — / 100  
**Last updated:** 2026-10-13

---

## Must-know definitions

| Term | 1–2 line definition |
|---|---|
| AI | Machines performing tasks that typically need human intelligence |
| ML | Systems that learn patterns from data instead of fixed rules |
| DL | ML using multi-layer neural networks |
| Generative AI | Models that *create* new content (text, images, code, audio) |
| LLM | Generative language model that predicts the next token |
| Discriminative model | Predicts a label/class for existing input (e.g. spam filter) |
| Generative model | Produces new samples similar to training data (e.g. email writer) |
| Hallucination | Confident but false output — model optimizes likelihood, not truth |
| Token | Chunk of text (word/subword) that the model reads and predicts |
| Virtual environment | Isolated Python dependency folder (here: `.venv`) |

## Core ideas (bullets only)

**Day 1**
- Nesting: **AI ⊃ ML ⊃ DL ⊃ GenAI ⊃ LLM**
- LLM generation loop: context → next-token probs → sample → append → repeat
- Toy word model ≈ same idea as ChatGPT, but 1-word context + count tables instead of Transformers
- GenAI strengths: draft, summarize, code help, structure messy text
- GenAI weaknesses: exact math, private/fresh facts, guaranteed truth → later fixed by **tools / RAG / evals**

**Days 2–6** _(fill as you complete)_
- Day 2: str/int/float/bool · indexing/slicing · f-strings · strip/lower; **punctuation still breaks uniqueness**
- Day 3: collections & loops …
- Day 4: functions, files, venv/pip …
- Day 5: classes …
- Day 6: P0 + Weekly Test 1 …

## Diagrams to redraw from memory
- [ ] AI family tree — `04-diagrams/flows/ai-family-tree.mmd`
- [ ] Next-token generation loop — `04-diagrams/flows/next-token-generation-loop.mmd`

## Corrected Q&A (wrong → right)
| Q | My wrong/partial answer | Ideal answer |
|---|---|---|
| Order AI/ML/DL/GenAI/LLM | AI > ML > GenAI > LLM (skipped DL) | AI → ML → **DL** → GenAI → LLM |
| What LLM does when generating | "predicts next tokens" | Predicts **and samples** next token given context so far |
| Toy vs ChatGPT | Context size + less training data (good start) | Also: 1-word context vs long context; **count tables vs Transformer weights** |
| Hallucination | Correct (spelling: hallucination) | Likelihood ≠ truth |
| Payroll + LLM alone | Correct — use Calculator API with LLM | Tool calling pattern (Week 13) |

## Code snippets to remember
```python
from collections import Counter, defaultdict
next_words = defaultdict(Counter)
for current, nxt in zip(words, words[1:]):
    next_words[current][nxt] += 1
# generate: random.choices(options, weights=counts)
```

## Decisions logged
- Knowledge layout: day work lives under `01-daily/`; durable revision under `08-revision/`
- Day 1 code placed in `01-daily/week-01/day-01/code/` (not a flat `week01/` folder)

## Mistakes / weak areas
- [ ] Pending Day 1 Q&A evaluation

## Resources worth rewatching (≤ 3)
1. [3Blue1Brown — LLMs explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) (8m)
2. [Google Cloud Tech — Intro to Generative AI](https://www.youtube.com/watch?v=G2fqAlgmoPo) (22m)

## Source daily folders
- [`01-daily/week-01/day-01/`](../../01-daily/week-01/day-01/)
