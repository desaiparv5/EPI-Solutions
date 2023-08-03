import random
import string
from heap import MinHeap


def random_string_generator():
    for _ in range(1000):
        yield "".join(random.choices(string.ascii_lowercase, k=random.randint(5, 100)))


def k_longest_strings(stream_data, k):
    heap = MinHeap()
    for s in stream_data:
        if len(heap) < k:
            heap.heappush(s)
            continue
        if len(heap.smallest()) < len(s):
            heap.heappop()
            heap.heappush(s)
    out_list = []
    while heap:
        out_list.append(heap.heappop())
    
    return out_list


def main():
    print(k_longest_strings(random_string_generator(), 10))


if __name__ == "__main__":
    main()

