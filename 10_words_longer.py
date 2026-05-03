
import random
import re
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python test-regedit.py <pathname>")
        return

    pathname = sys.argv[1]

    try:
        with open(pathname, "r", encoding="utf-8") as file:
            raw_text = file.read()
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        text = raw_text.lower()
    except Exception as e:
        print(f"Error: {e}")
        return

    # Regex finds letter-only words; length filter keeps words over 10 letters.
    try:
        words = re.findall(r"[a-zA-Z]+", text)
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        unique_long_words = sorted({word for word in words if len(word) > 10})
    except Exception as e:
        print(f"Error: {e}")
        return

    if len(unique_long_words) < 10:
        print("Fewer than ten matching words found.")
        return

    try:
        chosen_words = random.sample(unique_long_words, 10)
    except Exception as e:
        print(f"Error: {e}")
        return

    for word in chosen_words:
        try:
            print(word)
        except Exception as e:
            print(f"Error: {e}")
            return


if __name__ == "__main__":
    main()
