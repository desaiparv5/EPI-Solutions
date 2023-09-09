from collections import Counter
from heaps.heap import MinHeap


class WordFrequency:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __gt__(self, _obj: "WordFrequency"):
        if self.frequency == _obj.frequency:
            return self.word < _obj.word
        return self.frequency >_obj.frequency

    def __le__(self, _obj: "WordFrequency"):
        if self.frequency == _obj.frequency:
            return self.word >= _obj.word
        return self.frequency <= _obj.frequency


def most_frequent_words(words_list, k):
    freq = Counter(words_list)
    heap = MinHeap()
    for key, val in freq.items():
        word_freq_obj = WordFrequency(key, val)
        if len(heap) < k:
            heap.heappush(word_freq_obj)
            continue
        if heap.smallest() < word_freq_obj:
            heap.heappop()
            heap.heappush(word_freq_obj)
    out_list = []
    while heap:
        out_list.append(heap.heappop().word)

    return out_list


def main():
    words_list = ["i","love","leetcode","i","love","coding"]
    k = 3
    print(most_frequent_words(words_list, k))


if __name__ == "__main__":
    main()
