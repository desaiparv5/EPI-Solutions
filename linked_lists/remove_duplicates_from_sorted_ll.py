from linked_list import LinkedList, Node


def remove_duplicates_from_sorted_linked_list(ll: LinkedList) -> None:
    pointer = ll.head
    assert ll.head
    advanced_pointer = ll.head.next
    while pointer and advanced_pointer and advanced_pointer.next:
        if pointer.val == advanced_pointer.val:
            advanced_pointer = advanced_pointer.next
        else:
            pointer.next = advanced_pointer
            pointer = pointer.next
            advanced_pointer = advanced_pointer.next
    assert pointer and advanced_pointer
    if advanced_pointer.next == None and pointer.next != advanced_pointer:
        pointer.next = None
        ll.tail = pointer

def main():
    ll = LinkedList([1,1,2,3,3,4,4,4,5,6,7,7,7])
    remove_duplicates_from_sorted_linked_list(ll)
    print(ll)


if __name__ == "__main__":
    main()
