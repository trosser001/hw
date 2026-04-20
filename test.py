import random
import sys


def extract_candidate_words(pathname):
    """Return unique words that are letters-only and longer than 10 chars."""
    candidates = set()

    with open(pathname, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_chars = []
            for ch in line.lower():
                cleaned_chars.append(ch if ch.isalpha() else " ")

            for word in "".join(cleaned_chars).split():
                if len(word) > 10:
                    candidates.add(word)

    return list(candidates)


def main():
    if len(sys.argv) != 2:
        print("what was entered: python test.py <pathname>")
        return

    pathname = sys.argv[1]

    try:
        words = extract_candidate_words(pathname)
    except FileNotFoundError:
        print("File not found.")
        return
    except PermissionError:
        print("File not readable.")
        return
    except UnicodeDecodeError:
        print("File is not encoded in UTF-8.")
        return

    if len(words) < 10:
        print("Fewer than ten matching words found.")
        return

    for word in random.sample(words, 10):
        print(word)


if __name__ == "__main__":
    main()
