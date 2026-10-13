"""
Week 1 Day 1 — Toy next-word language model.

Core idea: an LLM generates text by predicting the next token.
This script uses word-level counts instead of a neural network.
"""

from collections import Counter, defaultdict
import random


corpus = """i love machine learning . i love generative ai .
generative ai creates new text . machine learning learns from data ."""

words = corpus.split()
next_words: dict[str, Counter] = defaultdict(Counter)

for current, nxt in zip(words, words[1:]):
    next_words[current][nxt] += 1


def predict_next(word: str) -> dict[str, float]:
    """Return probability distribution over words that follow `word`."""
    counts = next_words[word]
    total = sum(counts.values())
    if total == 0:
        return {}
    return {w: round(c / total, 2) for w, c in counts.most_common()}


def generate(start: str, length: int = 8) -> str:
    """Sample a short continuation starting from `start`."""
    out = [start]
    for _ in range(length):
        options = next_words[out[-1]]
        if not options:
            break
        out.append(random.choices(list(options), weights=list(options.values()))[0])
    return " ".join(out)


if __name__ == "__main__":
    print("P(next | 'love') =", predict_next("love"))
    print("P(next | 'learning') =", predict_next("learning"))
    print("\nFive generations from 'i':")
    for i in range(1, 6):
        print(f"  {i}. {generate('i')}")
