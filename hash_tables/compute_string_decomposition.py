from collections import Counter


def compute_string_decompositions(text, words):
    words_freq = Counter(words)
    word_len = len(words[0])
    def match_words_in_dict(start):
        curr_freq = Counter()
        for i in range(start, start + word_len * len(words), word_len):
            sub = text[i:i+word_len]
            if words_freq[sub] == 0:
                return False
            curr_freq[sub] += 1
            if curr_freq[sub] > words_freq[sub]:
                return False
        return True

    return [i for i in range(len(text) - len(words) * word_len + 1) if match_words_in_dict(i)]


def main():
    text = "amanaplanacanasa"
    words = ["can", "apl", "ana"]
    print(compute_string_decompositions(text, words))


if __name__ == "__main__":
    main()
