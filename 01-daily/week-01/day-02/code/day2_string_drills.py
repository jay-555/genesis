"""
Week 1 Day 2 — String drills for GenAI / NLP prep.

Complete every TODO. Run:
  python 01-daily/week-01/day-02/code/day2_string_drills.py
"""


def main() -> None:
    # --- 1. Variables & types ---
    model_name = "gpt-4o-mini"
    max_tokens = 512
    temperature = 0.7
    streaming = True

    print("TYPES")
    print(type(model_name), type(max_tokens), type(temperature), type(streaming))

    # --- 2. Indexing & slicing ---
    s = "Generative"
    # TODO: print first char, last char, and slice "ener"
    print("\nINDEX / SLICE")
    print("first:", s[0])  # expected: G
    print("last:", s[-1])  # expected: e
    print("slice 1:4:", s[1:4])  # expected: ene  (wait — "ener" is s[1:5])
    # Fix the slice yourself if you want "ener":
    print("ener?:", s[1:5])  # expected: ener

    # --- 3. Useful string methods ---
    raw = "  Hello GenAI World!  "
    cleaned = raw.strip().lower()
    words = cleaned.split()
    joined = "-".join(words)

    print("\nMETHODS")
    print("cleaned:", repr(cleaned))
    print("words:", words)
    print("joined:", joined)
    print("replace:", cleaned.replace("genai", "generative-ai"))
    print("startswith hello?:", cleaned.startswith("hello"))

    # --- 4. f-strings ---
    name = "GPT"
    price = 0.03
    # TODO: change this to an f-string: Model GPT costs $0.03
    message = f"Model {name} costs ${price}"
    print("\nF-STRING")
    print(message)

    # --- 5. Mini GenAI-style cleanup ---
    prompts = [
        "  Summarize this PDF. ",
        "SUMMARIZE THIS PDF.",
        "summarize this pdf",
    ]
    # TODO: normalize all prompts the same way (strip + lower)
    # then print how many unique prompts remain
    normalized = [p.strip().lower() for p in prompts]
    unique = set(normalized)
    print("\nPROMPT NORMALIZE")
    print("normalized:", normalized)
    print("unique count:", len(unique))  # expected: 1

    # --- 6. Your turn ---
    # TODO: take any sentence; print word count and character count (excluding spaces)
    sentence = "Large language models predict the next token."
    word_count = len(sentence.split())
    char_count_no_spaces = len(sentence.replace(" ", ""))
    print("\nYOUR TURN")
    print("sentence:", sentence)
    print("words:", word_count)
    print("chars (no spaces):", char_count_no_spaces)


if __name__ == "__main__":
    main()
