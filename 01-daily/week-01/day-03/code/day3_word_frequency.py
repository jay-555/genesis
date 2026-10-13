"""
Week 1 Day 3 — Word frequency counter.

Skills: list, dict, set, loops, comprehensions, light text cleaning.
Run:
  python 01-daily/week-01/day-03/code/day3_word_frequency.py
"""

from collections import Counter
import string


SAMPLE = """
Generative AI creates new text. Large language models predict the next token.
Generative AI is a type of deep learning. Language models learn from data.
I love machine learning and I love generative AI.
"""


def clean_and_tokenize(text: str) -> list[str]:
    """Lowercase, remove punctuation, split into words."""
    text = text.lower()
    # remove punctuation (Day 2 lesson: strip+lower is not enough)
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words


def count_with_dict(words: list[str]) -> dict[str, int]:
    """Count words using a plain dict (you should understand this deeply)."""
    freq: dict[str, int] = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
        # equivalent one-liner style: freq[w] = freq.get(w, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Return top-n (word, count) pairs, highest count first."""
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)[:n]


def main() -> None:
    words = clean_and_tokenize(SAMPLE)
    print("TOKENS (first 15):", words[:15])
    print("Total tokens:", len(words))
    print("Unique words (set):", len(set(words)))

    freq = count_with_dict(words)
    print("\nFREQ (dict sample):", {k: freq[k] for k in list(freq)[:8]})

    print("\nTOP 5 (manual dict):")
    for word, count in top_n(freq, 5):
        print(f"  {word}: {count}")

    # Counter is the standard library shortcut — same idea as our dict loop
    print("\nTOP 5 (collections.Counter):")
    for word, count in Counter(words).most_common(5):
        print(f"  {word}: {count}")

    # Comprehension practice: words longer than 7 characters
    long_words = [w for w in set(words) if len(w) > 7]
    print("\nLong unique words (>7 chars):", sorted(long_words))

    # TODO (optional stretch): ignore stopwords {"a", "the", "and", "of", "is", "i"}
    stop = {"a", "the", "and", "of", "is", "i"}
    filtered = [w for w in words if w not in stop]
    print("\nTOP 5 without stopwords:")
    for word, count in Counter(filtered).most_common(5):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
