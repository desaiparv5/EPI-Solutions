from abc import ABC, abstractmethod
import typing


class Heap(ABC):
    def __init__(self):
        self._list = []

    def __len__(self) -> int:
        return len(self._list)

    def __repr__(self) -> str:
        return ", ".join(self._list)

    def __str__(self) -> str:
        return self.__repr__()

    def __bool__(self) -> bool:
        return bool(len(self))

    def __left_child_index(self, parent_index : int) -> int:
        return 2 * parent_index + 1

    def __right_child_index(self, parent_index : int) -> int:
        return 2 * parent_index + 2

    def __parent_index(self, child_index : int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, parent_index : int) -> bool:
        return self.__left_child_index(parent_index) < len(self)

    def __has_right_child(self, parent_index : int) -> bool:
        return self.__right_child_index(parent_index) < len(self)

    def __has_parent(self, child_index : int) -> bool:
        return self.__parent_index(child_index) >= 0

    def _left_child(self, parent_index : int) -> typing.Union[typing.Any, None]:
        if not self.__has_left_child(parent_index):
            return
        else:
            return self._list[self.__left_child_index(parent_index)]

    def _right_child(self, parent_index : int) -> typing.Union[typing.Any, None]:
        if not self.__has_right_child(parent_index):
            return
        else:
            return self._list[self.__right_child_index(parent_index)]

    def _parent(self, child_index : int) -> typing.Union[typing.Any, None]:
        if not self.__has_parent(child_index):
            return
        else:
            return self._list[self.__parent_index(child_index)]

    def _swap_elements(self, posa, posb):
        self._list[posa], self._list[posb] = self._list[posb], self._list[posa]

    def _heapify_left_side(self, index: int) -> None:
        left_index = self.__left_child_index(index)
        self._swap_elements(index, left_index)
        self._heapify_down(left_index)

    def _heapify_right_side(self, index: int) -> None:
        right_index = self.__right_child_index(index)
        self._swap_elements(index, right_index)
        self._heapify_down(right_index)
    
    def _heapify_parent(self, index) -> None:
        parent_index = self.__parent_index(index)
        self._swap_elements(parent_index, index)
        self._heapify_up(parent_index)

    def heappush(self, val: typing.Any) -> None:
        self._list = self._list + [val]
        self._heapify_up(len(self) - 1)    

    def heappop(self) -> typing.Any:
        val = self._list[0]
        if self._list:
            self._swap_elements(0, -1)
            self._list = self._list[:-1]
            self._heapify_down(0)
        return val
    
    def peek(self) -> typing.Any:
        if self:
            return self._list[0]

    @abstractmethod
    def _heapify_up(self, index: int):
        pass

    @abstractmethod
    def _heapify_down(self, index: int):
        pass


class MaxHeap(Heap):
    def _heapify_up(self, index: int):
        parent = self._parent(index)
        if parent is None:
            return
        elif parent < self._list[index]:
            self._heapify_parent(index)

    def _heapify_down(self, index: int):
        left_child = self._left_child(index)
        right_child = self._right_child(index)

        if left_child is None and right_child is None:
            return
        if left_child is not None and left_child >= self._list[index]:
            self._heapify_left_side(index)
        if  right_child is not None and right_child >= self._list[index]:
            self._heapify_right_side(index)
    
    def largest(self):
        if self:
            return self._list[0]


class MinHeap(Heap):
    def _heapify_up(self, index: int):
        parent = self._parent(index)
        if parent is None:
            return
        elif parent > self._list[index]:
            self._heapify_parent(index)

    def _heapify_down(self, index: int):
        left_child = self._left_child(index)
        right_child = self._right_child(index)

        if left_child is None and right_child is None:
            return
        if left_child is not None and left_child <= self._list[index]:
            self._heapify_left_side(index)
        if  right_child is not None and right_child <= self._list[index]:
            self._heapify_right_side(index)

    def smallest(self) -> typing.Any:
        if self:
            return self._list[0]
