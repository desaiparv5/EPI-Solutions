from stack_and_queue import Stack


def buildings_with_sunset(buildings):
    # GIVEN
    # buildings are in order east to west
    # sun sets in west
    stack = Stack()

    for building in buildings:
        while stack and building >= stack.peek():
            stack.pop()
        stack.push(building)
    return [_ for _ in stack]


def main():
    buildings = [4,3,2,1,5]
    print(buildings_with_sunset(buildings))


if __name__ == "__main__":
    main()
