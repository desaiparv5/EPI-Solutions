import typing
from stack_and_queue import QueueInteface
scaling_factor = 2


class CircularQueue(QueueInteface):
    def __init__(self, capacity):
        if capacity <= 0:
            raise Exception
        self._values = [None] * capacity
        self._head = 0
        self._tail = 0
        self._num_elements = 0

    def enqueue(self, val):
        if self._num_elements == len(self._values):
            self._values = self._values[self._head:] + self._values[:self._head]
            self._values = self._values + [None] * (len(self._values) * (scaling_factor - 1))
            self._head, self._tail = 0, self._num_elements

        self._values[self._tail] = val
        self._num_elements += 1
        self._tail = (self._tail + 1) % len(self._values)

    def dequeue(self):
        val = self._values[self._head]
        self._values[self._head] = None
        self._head = (self._head + 1) % len(self._values)
        self._num_elements -= 1
        return val
    
    def peek(self) -> typing.Any:
        return self._values[self._head]

    def __repr__(self) -> str:
        return f"[{', '.join(['' if not value else str(value) for value in self._values])}]"


def implment_circular_queue():
    queue = CircularQueue(4)
    # use debugger to test
    print(queue)


def main():
    implment_circular_queue()


if __name__ == "__main__":
    main()
