# Week 01 · Day 01 — Notes

**Date:** 2026-10-12  
**Topic:** The big picture — AI → ML → DL → GenAI → LLM; environment setup  
**Section:** A — Foundations  
**Study time:** ~75 min  
**Resources used:**
- [Google Cloud Tech — Introduction to Generative AI](https://www.youtube.com/watch?v=G2fqAlgmoPo) (22m)
- [3Blue1Brown — LLMs explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) (8m)
- Optional: [5 Minutes Engineering — What is Generative AI](https://www.youtube.com/watch?v=5l7Tw6UVQi8) (9m)

---

## What I need to understand
- Where Generative AI sits inside AI / ML / DL
- What an LLM actually does (next-token prediction)
- Why LLMs can hallucinate
- How to set up a Python virtual environment for this course

## Concepts (simple language)
AI is nested circles: **AI ⊃ ML ⊃ DL ⊃ GenAI ⊃ LLM**.

- **AI:** machines doing tasks that need "intelligence"
- **ML:** learn patterns from examples instead of hand-written rules
- **DL:** ML using many-layered neural networks
- **Generative AI:** DL models that *create* new content
- **LLM:** GenAI for language — predicts the next token

**Discriminative vs generative:**
- Discriminative → classifies / predicts a label (spam filter)
- Generative → produces new data that looks like the training data (email writer)

## Analogy
Teaching someone to cook:
- Classic AI = recipe rulebook
- ML = learn from 10,000 dishes
- DL = deeper "brain" catching subtle patterns
- GenAI = invents a *new* recipe

## Technical definition
A **Large Language Model** is a Transformer-based neural network trained on large text corpora to model the probability of the next token given previous tokens.

## Examples
Prompt: `"The capital of France is"`  
Model assigns probabilities such as `Paris ≈ 0.92`, then samples and continues.

Toy next-word model: see `code/day1_next_word.py`.

## Code I wrote / studied
- Path: `code/day1_next_word.py`
- What it does: counts word→next-word frequencies and generates text by sampling

## Key takeaways (max 5)
1. GenAI creates; classic ML often classifies/predicts.
2. LLMs generate by repeated next-token prediction — not by looking up facts.
3. Hallucinations happen because the model optimizes for *likelihood*, not *truth*.
4. Weaknesses (math, private data, truth) are fixed later by tools / RAG / evals.
5. Always use a virtual environment (`.venv`) for project isolation.

## Still unclear
- (fill after Day 1 Q&A feedback)

## Links to diagrams / references
- Diagram: `diagrams/ai-family-tree.mmd`
- Promoted: `04-diagrams/flows/ai-family-tree.mmd`
- Revision: `08-revision/by-week/week-01.md`
