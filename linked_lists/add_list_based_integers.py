from linked_list import LinkedList, Node


def add_list_based_integers(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    out_ll = LinkedList()
    node1 = ll1.head
    node2 = ll2.head
    carry = 0
    while node1 or node2:
        new_val = carry
        if node1:
            new_val += node1.val
            node1 = node1.next
        if node2:
            new_val += node2.val
            node2 = node2.next
        out_ll.add_tail(new_val % 10)
        carry = new_val // 10
    if carry:
        out_ll.add_tail(carry)
    return out_ll


def main():
    ll1 = LinkedList([1,7])
    ll2 = LinkedList([1,2,3])
    out_ll = add_list_based_integers(ll1, ll2)
    print(out_ll)


if __name__ == "__main__":
    main()
