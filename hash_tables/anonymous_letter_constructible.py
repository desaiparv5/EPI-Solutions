from collections import Counter


def is_ananymous_letter_constructible(letter_text, magazine_text):
    anon_letters_count = Counter(letter_text)

    for char in magazine_text:
        if char in anon_letters_count:
            anon_letters_count[char] -= 1
            if not anon_letters_count[char]:
                anon_letters_count.pop(char)
        if anon_letters_count == {}:
            return True
    return False


def is_ananymous_letter_constructible_pythonic(letter_text, magazine_text):
    return not Counter(letter_text) - Counter(magazine_text)


def main():
    letter_text = "get izzt"
    magazine_text = "this is magazine text"
    print(is_ananymous_letter_constructible_pythonic(letter_text, magazine_text))


if __name__ == "__main__":
    main()
