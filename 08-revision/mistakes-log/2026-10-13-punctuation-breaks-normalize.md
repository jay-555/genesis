# Insight: strip + lower is not full normalization

**Date:** 2026-10-13  
**Week/Day:** W1 D2  
**Category:** Code / NLP preview

## What happened
Prompt normalize gave `unique count: 2` instead of 1.

## Why
`"summarize this pdf."` ≠ `"summarize this pdf"` — trailing period survived `.strip().lower()`.

## Correct understanding
For duplicate detection / Bag-of-Words style counting, often also remove or normalize punctuation.

## How I'll remember it
Clean pipeline ≈ lower → strip → remove punctuation → (optional) stopwords.

## Related
Day 3 `clean_and_tokenize()` uses `string.punctuation`.
