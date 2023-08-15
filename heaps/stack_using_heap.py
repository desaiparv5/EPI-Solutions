import typing
from heap import MaxHeap
from stacks_and_queues.stack_and_queue import StackInterface


class StackUsingHeap(StackInterface):
    def __init__(self) -> None:
        self._max_heap = MaxHeap()
    
    def push(self, val) -> None:
        if len(self._max_heap) == 0:
            curr_idx = 0
        else:
            curr_idx = self._max_heap.peek()[0] + 1
        self._max_heap.heappush((curr_idx, val))
    
    def pop(self) -> typing.Any:
        return self._max_heap.heappop()[1]
    
    def peek(self) -> typing.Any:
        return self._max_heap.peek()[1]


def stack_using_heap():
    stack = StackUsingHeap()
    pass


def main():
    stack_using_heap()


if __name__ == "__main__":
    main()
