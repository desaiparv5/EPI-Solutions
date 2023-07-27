import typing
from linked_list import LinkedList, Node


def linked_list_cycle_length(start: Node) -> int:
    curr_node = start.next
    length = 1
    while curr_node is not start:
        length += 1
        assert curr_node
        curr_node = curr_node.next
    return length


def linked_list_cyclicity(ll: LinkedList) -> typing.Union[None, Node]:
    slow_pointer = ll.head
    assert ll.head and ll.head.next
    fast_pointer = ll.head.next.next

    while fast_pointer and fast_pointer.next and fast_pointer.next.next:
        if slow_pointer is fast_pointer:
            return slow_pointer
        fast_pointer = fast_pointer.next.next
        assert slow_pointer
        slow_pointer = slow_pointer.next
    return None


def introduce_cycle_in_linked_list(ll: LinkedList, ind: int) -> None:
    start, end = ll.head, ll.head
    for _ in range(ind):
        assert start
        start = start.next
    while end and end.next:
        end = end.next
    assert end
    end.next = start


def start_of_cycle(ll: LinkedList, cycle_length: int) -> Node:
    advanced_pointer = ll.head
    for _ in range(cycle_length):
        assert advanced_pointer
        advanced_pointer = advanced_pointer.next

    slow_pointer = ll.head
    while slow_pointer is not advanced_pointer:
        assert slow_pointer and advanced_pointer
        slow_pointer = slow_pointer.next
        advanced_pointer = advanced_pointer.next
    assert slow_pointer
    return slow_pointer


def main():
    ll = LinkedList([1,2,3,4,5,6,7,8])
    introduce_cycle_in_linked_list(ll, 4)

    is_cycle = linked_list_cyclicity(ll)

    if is_cycle:
        print("Linked list contains cycle")
        cycle_length = linked_list_cycle_length(is_cycle)
        print(f"Length of cycle: {cycle_length}")
        cycle_start = start_of_cycle(ll, cycle_length)
        print(f"Node {cycle_start} is start of cycle")
    else:
        print("Linked list does not contain a cycle")


if __name__ == "__main__":
    main()
