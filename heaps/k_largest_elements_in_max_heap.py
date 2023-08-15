from heap import MaxHeap
from collections import namedtuple


def k_largest_elements_in_max_heap(max_heap: MaxHeap, k) -> list:
    result = []
    candidate_max_heap = MaxHeap()
    candidate_max_heap.heappush((max_heap._list[0], 0))
    for _ in range(k):
        candidate_index = candidate_max_heap._list[0][1]
        result.append(candidate_max_heap.heappop()[0])

        left_index = candidate_index * 2 + 1
        if left_index < len(max_heap):
            candidate_max_heap.heappush((max_heap._list[left_index], left_index))

        right_index = candidate_index * 2 + 2
        if right_index < len(max_heap):
            candidate_max_heap.heappush((max_heap._list[right_index], right_index))

    return result

def main():
    max_heap = MaxHeap()
    for val in range(10):
        max_heap.heappush(val)
    k = 4
    print(k_largest_elements_in_max_heap(max_heap, k))


if __name__ == "__main__":
    main()
