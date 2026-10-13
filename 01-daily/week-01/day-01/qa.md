# Week 01 · Day 01 — Q&A

**Date:** 2026-10-12 (closed 2026-10-13)  
**Topic:** AI family tree, next-token prediction, hallucinations  
**Status:** Completed  
**Day score:** 6 / 7 Correct-or-Partial · **Gate:** Pass → Day 2

---

## Understanding check (mentor questions)

### Q1
**Question:** Order these from broadest to narrowest: DL, AI, LLM, ML, GenAI.  
**My answer:**  
AI > ML > GenAI > LLM

**Correct / Ideal answer:**  
AI → ML → DL → GenAI → LLM  

**Status:** Partial  
**What I learned:** Deep Learning (DL) sits between ML and GenAI. Don’t skip it — GenAI is a type of DL.

### Q2
**Question:** A spam filter and an email-writing assistant: which is generative, and why?  
**My answer:** Email-writing assistant is generative - as it creates new text where as Spam filter is discriminative - it lables existing text;

**Correct / Ideal answer:**  
Email-writing assistant is generative — it *creates* new text. Spam filter is discriminative — it labels existing text.  

**Status:** Correct  
**What I learned:** Create = generative; classify/label = discriminative.

### Q3
**Question:** In one sentence, what does an LLM do when it generates text?  
**My answer:** it repeatedly predicts the next possible tokens  

**Correct / Ideal answer:**  
It repeatedly predicts (and samples) the next token given the tokens so far.  

**Status:** Partial (close — add *sampling*)  
**What I learned:** Prediction gives probabilities; **sampling** picks the actual next token (why answers can vary — see Q7).

### Q4
**Question:** Our toy model and ChatGPT both predict the next word. Name two important differences.  
**My answer:** Context size, Less training data  

**Correct / Ideal answer:**  
(1) Context: toy model looks at 1 previous word; LLMs attend over thousands of tokens.  
(2) Representation: toy model uses simple counts; LLMs use billions of learned parameters (Transformer).  
Also: vocabulary size, training data scale, sampling controls (temperature, top-p).  

**Status:** Partial (right direction — also: counts vs neural weights / Transformer)  
**What I learned:** Bigger context + more data matter; LLMs also learn rich parameters, not just word-count tables.

### Q5
**Question:** Why can an LLM state something false with full confidence?  
**My answer:** This is called hallucination. Actually LLMs do not know about right or wrong; they only predict the next possible tokens  

**Correct / Ideal answer:**  
It optimizes for plausible next tokens (likelihood), not verified truth. Confident-sounding false text is a hallucination.  

**Status:** Correct  
**What I learned:** Spelling: **hallucination**. Likelihood ≠ truth.

### Q6
**Question (scenario):** Manager wants an LLM alone to calculate exact monthly payroll for 5,000 employees. Concern + suggestion?  
**My answer:** Yes concern because LLMs are bad at math. I will suggest to use Calculator API along with LLMs for efficient performance  

**Correct / Ideal answer:**  
Concern: LLMs are weak at exact arithmetic and may hallucinate numbers.  
Suggestion: use deterministic code/tools (spreadsheet, calculator API, payroll system) via tool/function calling; LLM can orchestrate, not compute totals.  

**Status:** Correct  
**What I learned:** LLM + tools (Week 13) — model plans; tools compute.

### Q7
**Question:** Share output of `generate("i")` (5 runs) and hallucination-hunt notes.  
**My answer:**  
```
1. i love machine learning . i love machine learning
2. i love generative ai creates new text . i
3. i love generative ai creates new text . generative
4. i love machine learning learns from data . generative
5. i love generative ai creates new text . generative
```

**Correct / Ideal answer:**  
Outputs should vary (sampling). Hallucination hunt should show invented paper details when asked about a fake paper.  

**Status:** Correct (code run + varied outputs proven)  
**What I learned:** Same start word → different continuations because of random sampling — same idea as temperature in real LLMs. (Optional: still try a fake-paper hallucination hunt once.)

---

## Profile questions (for pacing)
| Question | My answer |
|---|---|
| Python level (never / basics / comfortable) | basic |
| Any ML exposure? | a little |
| LLM API access (Azure OpenAI / Gemini / OpenAI / none yet)? | Used Gemini API once |
| ~1–1.5h weekdays + ~3h Saturday OK? | Yes |
| Hindi videos OK or English only? | Prefer English (Hindi OK sometimes) |

---

## My own questions
| # | Question | Answer / resolution | Promote to interview bank? |
|---|---|---|---|
| 1 | | | |
