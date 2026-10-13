# AI → ML → DL → GenAI → LLM

**Source:** Week 1 Day 1 · **Status:** Draft (pending your Q&A)  
**Diagram:** [`../../04-diagrams/flows/ai-family-tree.mmd`](../../04-diagrams/flows/ai-family-tree.mmd)

## Nesting
`AI ⊃ ML ⊃ DL ⊃ Generative AI ⊃ LLM`

## Discriminative vs generative
| | Discriminative | Generative |
|---|---|---|
| Job | Label / predict | Create new content |
| Example | Spam filter | Email-writing assistant |

## LLM core loop
1. Read context tokens  
2. Compute next-token probability distribution  
3. Sample a token (temperature / top-p later)  
4. Append and repeat  

## Hallucinations
Models maximize *plausibility*, not verified truth → confident falsehoods possible.

## Practical implication
Do not use an LLM alone for exact payroll/math or private company facts. Use **tools**, **RAG**, and **evals** later in the curriculum.
