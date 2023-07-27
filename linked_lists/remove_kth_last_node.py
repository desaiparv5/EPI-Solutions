from linked_list import LinkedList, Node


def remove_kth_last_node(ll: LinkedList, k: int) -> None:
    if k <= 0:
        raise Exception
    if k == 1:
        ll.delete_tail()
    else:
        advanced_pointer = ll.head
        while advanced_pointer and k > 1:
            advanced_pointer = advanced_pointer.next
            k -= 1

        if k and not advanced_pointer:
            raise Exception
        dummy_node = Node(None, next=ll.head)
        pointer = dummy_node
        while advanced_pointer and pointer and advanced_pointer.next:
            advanced_pointer = advanced_pointer.next
            pointer = pointer.next
        if pointer and pointer.next == ll.head:
            ll.delete_head()
        else:
            assert pointer
            ll.delete_next_node(pointer)

def main():
    ll = LinkedList([1,2,3,4,5,6,7,8,9,10])
    k = 10
    remove_kth_last_node(ll, k)
    print(ll)


if __name__ == "__main__":
    main()
