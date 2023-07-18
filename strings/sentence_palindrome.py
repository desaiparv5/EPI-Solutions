def is_sentence_palindrome(sentence: str):
    i = 0
    j = len(sentence) - 1
    while i < j:
        while not sentence[i].isalnum() and i < j:
            i += 1
        while not sentence[j].isalnum() and i < j:
            j -= 1
        if sentence[i].lower() != sentence[j].lower():
            return False
        i += 1
        j -= 1
    return True


def main():
    sentence = "Able was I, ere I saw Elba!"
    print(is_sentence_palindrome(sentence))


if __name__ == "__main__":
    main()
