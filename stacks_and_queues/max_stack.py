from stack_and_queue import Stack


class MaxStruct:
    def __init__(self, max_value):
        self.max_value = max_value
        self.count = 1


class MaxStack:
    def __init__(self):
        self._stack = Stack()
        self._max_cache = Stack()

    def max(self):
        if self._max_cache and self._stack:
            max_value: MaxStruct = self._max_cache.peek()
            return max_value.max_value
    
    def pop(self):
        if not self._max_cache or not self._stack:
            return
        max_value: MaxStruct = self._max_cache.peek()
        if max_value.count > 1:
            max_value.count -= 1
        else:
            self._max_cache.pop()
        return self._stack.pop()
    
    def push(self, val):
        self._stack.push(val)
        max_value: MaxStruct = self._max_cache.peek()
        if not max_value or val > max_value.max_value:
            self._max_cache.push(MaxStruct(val))
        else:
            max_value.count += 1
    
    def __bool__(self):
        return bool(self._stack)


def max_stack_api():
    stack = MaxStack()
    # use debugger to test
    pass


def main():
    max_stack_api()


if __name__ == "__main__":
    main()
