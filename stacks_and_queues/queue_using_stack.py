import typing
from stack_and_queue import Stack, QueueInteface


class QueueUsingStack(QueueInteface):
    def __init__(self, values=None):
        self._enqueue_stack = Stack()
        self._dequeue_stack = Stack()

    def enqueue(self, val):
        self._enqueue_stack.push(val)

    def dequeue(self):
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.push(self._enqueue_stack.pop())
        if not self._dequeue_stack:
            raise Exception
        return self._dequeue_stack.pop()
    
    def peek(self) -> typing.Any:
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.push(self._enqueue_stack.pop())
        if not self._dequeue_stack:
            raise Exception
        return self._dequeue_stack.peek()
    

def queue_using_stack():
    queue = QueueUsingStack()
    # test this using debugger
    print(queue)


def main():
    queue_using_stack()


if __name__ == "__main__":
    main()
