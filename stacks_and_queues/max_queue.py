from stack_and_queue import Queue
from max_stack import MaxStack


class MaxQueue:
    def __init__(self):
        self._queue = Queue()
        self._max_queue = Queue()
    
    def enqueue(self, val):
        self._queue.enqueue(val)
        while self._max_queue and self._max_queue.peek() < val:
            self._max_queue.dequeue()
        self._max_queue.enqueue(val)


    def dequeue(self):
        if not self._queue:
            raise Exception
        res = self._queue.dequeue()
        if res == self._max_queue.peek():
            self._max_queue.dequeue()
        return res
    
    def max(self):
        return self._max_queue.peek()


class MaxQueueFromStack:
    def __init__(self):
        self._enqueue_stack = MaxStack()
        self._dequeue_stack = MaxStack()

    def enqueue(self, val):
        self._enqueue_stack.push(val)

    def dequeue(self, ):
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.push(self._enqueue_stack.pop())
        if not self._dequeue_stack:
            raise Exception
        return self._dequeue_stack.pop()

    def max(self):
        if self._enqueue_stack and self._dequeue_stack:
            return max(self._enqueue_stack.max(), self._dequeue_stack.max()) # type: ignore
        elif self._enqueue_stack:
            return self._enqueue_stack.max()
        elif self._dequeue_stack:
            return self._dequeue_stack.max()
        else:
            raise Exception


def implement_max_queue():
    queue = MaxQueue()
    queue = MaxQueueFromStack()
    # use debugger to test
    print(queue)


def main():
    implement_max_queue()


if __name__ == "__main__":
    main()
