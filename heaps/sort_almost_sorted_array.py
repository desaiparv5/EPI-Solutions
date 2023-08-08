from heap import MinHeap



def sort_k_sorted_array(array, k):
    heap = MinHeap()
    for i in range(k+1):
        heap.heappush(array[i])

    sorted_array = []
    curr_index = k + 1
    while heap:
        sorted_array.append(heap.heappop())
        if curr_index < len(array):
            heap.heappush(array[curr_index])
            curr_index += 1
    return sorted_array


def main():
    array = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    print(sort_k_sorted_array(array, k))


if __name__ == "__main__":
    main()
