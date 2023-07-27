from linked_list import LinkedList, Node


def linked_list_pivoting(ll: LinkedList, k: int) -> None:
    low_head = low_tail = Node("")
    equal_head = equal_tail = Node("")
    high_head = high_tail = Node("")
    
    for node in ll:
        if node.val < k:
            low_tail.next = node
            low_tail = low_tail.next
        elif node.val == k:
            equal_tail.next = node
            equal_tail = equal_tail.next
        else:
            high_tail.next = node
            high_tail = high_tail.next

    low_tail.next = equal_head.next
    equal_tail.next = high_head.next
    high_tail.next = None
    ll.head = low_head.next


def main():
    ll = LinkedList([3,6,2,8,7,2,1,3,5,7,9,3,2,1])
    k = 5
    linked_list_pivoting(ll, k)
    print(ll)


if __name__ == "__main__":
    main()
