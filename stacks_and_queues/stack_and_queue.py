import typing


class Stack:
    def __init__(self, values = None):
        self._stack: list = values if values else []

    def push(self, val) -> None:
        self._stack.append(val)

    def pop(self) -> typing.Any:
        if self:
            return self._stack.pop()
    
    def peek(self) -> typing.Any:
        if self:
            return self._stack[-1]

    def __bool__(self) ->    bool:
        return len(self._stack) > 0
    
    def __repr__(self):
        return ", ".join([str(x) for x in self._stack])

    def __iter__(self):
        for val in self._stack:
            yield val


class Queue:
    def __init__(self, values = None):
        self._queue: list = values if values else []

    def enqueue(self, val) -> None:
        self._queue.append(val)

    def dequeue(self) -> typing.Any:
        if self:
            return self._queue.pop(0)
    
    def peek(self) -> typing.Any:
        if self:
            return self._queue[0]

    def __bool__(self) ->    bool:
        return len(self._queue) > 0
    
    def __repr__(self):
        return f"[{', '.join([str(x) for x in self._queue])}]"

    def __iter__(self):
        for val in self._queue:
            yield val
    
    def __len__(self) -> int:
        return len(self._queue)
