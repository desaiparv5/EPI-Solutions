import typing
from linked_list import LinkedList, Node, DoublyLinkedList


def append_node(ll: LinkedList, node: Node) -> None:
    ll.add_tail(node.val)


def _merge_linked_lists(ll1: LinkedList, ll2: LinkedList, out_ll: LinkedList) -> typing.Union[DoublyLinkedList, LinkedList]:
    ptr1 = ll1.head
    ptr2 = ll2.head
    while ptr1 and ptr2:
        if ptr1.val > ptr2.val:
            append_node(out_ll, ptr2)
            ptr2 = ptr2.next
        else:
            append_node(out_ll, ptr1)
            ptr1 = ptr1.next
    while ptr1:
        append_node(out_ll, ptr1)
        ptr1 = ptr1.next
    while ptr2:
        append_node(out_ll, ptr2)
        ptr2 = ptr2.next
    return out_ll        


def merge_two_sorted_linked_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    out_ll = LinkedList([])
    return _merge_linked_lists(ll1, ll2, out_ll)


def merge_two_sorted_doubly_linked_list(ll1: DoublyLinkedList, ll2: DoublyLinkedList) -> DoublyLinkedList:
    out_ll = DoublyLinkedList([])
    return _merge_linked_lists(ll1, ll2, out_ll) # type: ignore


def main():
    ll1 = LinkedList([1, 3, 3, 3, 4 , 9, 11])
    ll2 = LinkedList([2, 3, 8])
    ll3 = merge_two_sorted_linked_lists(ll1, ll2)
    print(ll3)

    dll1 = DoublyLinkedList([1, 3, 3, 3, 4 , 9, 11])
    dll2 = DoublyLinkedList([2, 3, 8])
    dll3 = merge_two_sorted_doubly_linked_list(dll1, dll2)
    print(dll3)

if __name__ == "__main__":
    main()
