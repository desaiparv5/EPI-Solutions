from linked_list import LinkedList, Node


def reverse_a_sublist(ll: LinkedList, start: int, end: int) -> None:
    if start == end:
        return
    if end < 0 and end > len(ll):
        raise Exception("Invalid arguments")
    
    dummy_head = Node("", next=ll.head)
    sublist_head, curr_node = dummy_head, ll.head

    for _ in range(start - 1):
        assert sublist_head and curr_node
        sublist_head, curr_node = sublist_head.next, curr_node.next

    assert sublist_head
    sublist_iter = sublist_head.next
    for _ in range(end - start):
        assert sublist_iter
        temp = sublist_iter.next
        assert temp
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    ll.head = dummy_head.next

def main():
    ll = LinkedList([1,2,3,4,5,6,7,8,9])
    start = 1
    end = 9
    reverse_a_sublist(ll, start, end)
    print(ll)


if __name__ == "__main__":
    main()
