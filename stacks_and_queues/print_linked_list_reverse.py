from linked_lists.linked_list import LinkedList
from stack_and_queue import Stack


def print_linked_list_reverse(ll: LinkedList):
    stack = Stack([_ for _ in ll])
    while stack:
        print(stack.pop())


def main():
    ll = LinkedList([1,2,3,4,5,6,7,8,9])
    print_linked_list_reverse(ll)


if __name__ == "__main__":
    main()
