def reverse_words_in_sentence(sentence):
    def reverse_range(start, end):
        while start < end:
            sentence[start], sentence[end] = sentence[end], sentence[start]
            start += 1
            end -= 1

    reverse_range(0, len(sentence) - 1)
    curr_index = 0
    while curr_index < len(sentence):
        word_start = curr_index
        while curr_index < len(sentence) and sentence[curr_index] != " ":
            curr_index += 1
        reverse_range(word_start, curr_index - 1)
        curr_index += 1


def main():
    sentence = list("ram is costly")
    reverse_words_in_sentence(sentence)
    assert "".join(sentence) == "costly is ram"


if __name__ == "__main__":
    main()
