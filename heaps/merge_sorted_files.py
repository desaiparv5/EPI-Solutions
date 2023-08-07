from heap import MinHeap


class ListTraversal:
    def __init__(self, array):
        self._array = array
        self._curr_index = 0

    def __gt__(self, _obj: "ListTraversal"):
        return self.value > _obj.value

    def __lt__(self, _obj: "ListTraversal"):
        return self.value < _obj.value
    
    def __eq__(self, _obj: "ListTraversal"):
        return self.value == _obj.value

    @property
    def value(self):
        return self._array[self.curr_index]
    
    def inc_pointer(self):
        self._curr_index += 1
        if self._curr_index >= len(self._array):
            raise IndexError
    
    @property
    def curr_index(self):
        return self._curr_index


def merge_sorted_arrays(arrays):
    heap = MinHeap()
    for arr in arrays:
        if arr:
            heap.heappush(ListTraversal(arr))

    out_arr = []
    while heap:
        out_index: ListTraversal = heap.heappop()
        out_arr.append(out_index.value)
        try:
            out_index.inc_pointer()
            heap.heappush(out_index)
        except:
            continue

    return out_arr


def main():
    arrays = [[1,2,3],[2,2,2,8,10]]
    merged_array = merge_sorted_arrays(arrays)
    print(merged_array)


if __name__ == "__main__":
    main()
