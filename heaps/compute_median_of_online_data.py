from heap import MinHeap, MaxHeap


def median_of_online_data(data_stream):
    out_list = []

    small_heap = MaxHeap()
    large_heap = MinHeap()
    for data in data_stream:
        small_heap.heappush(data)
        if len(small_heap) > len(large_heap) + 1:
            large_heap.heappush(small_heap.heappop())
        if len(small_heap) == len(large_heap):
            out_list.append((small_heap.peek() + large_heap.peek())/2)
        else:
            out_list.append(small_heap.peek())

    return out_list


def main():
    data_stream = [2,7,0,1,5,6]
    print(median_of_online_data(data_stream))


if __name__ == "__main__":
    main()
