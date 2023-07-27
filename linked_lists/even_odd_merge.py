from linked_list import LinkedList, Node


def even_odd_merge(ll: LinkedList):
    if not ll.head or not ll.head.next:
        return ll
    even_head = even_tail = Node("")
    odd_head = odd_tail = Node("")
    
    parity = 0
    for node in ll:
        if parity:
            even_tail.next = node
            even_tail = even_tail.next
        else:
            odd_tail.next = node
            odd_tail = odd_tail.next
        parity ^= 1
    odd_tail.next = even_head.next
    even_tail.next = None
    ll.head = odd_head.next

def main():
    ll = LinkedList([1,2,3,4,5,6,7,8,9])
    even_odd_merge(ll)
    print(ll)


if __name__ == "__main__":
    main()
