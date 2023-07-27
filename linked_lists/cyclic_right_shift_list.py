from linked_list import LinkedList, Node
from overlapping_linked_list_w_cycle import advance_node_by_steps


def cylic_right_shift_linked_list(ll: LinkedList, k: int) -> None:
    linked_list_length = len(ll)
    k %= linked_list_length
    if not k:
        return
    
    dummy_head = Node("", next=ll.head)
    new_tail = advance_node_by_steps(dummy_head, linked_list_length - k)
    new_head = new_tail.next
    curr_node = new_head
    while curr_node and curr_node.next:
        curr_node = curr_node.next
    assert curr_node
    curr_node.next = ll.head
    ll.head = new_head
    ll.tail = new_tail
    new_tail.next = None


def main():
    ll = LinkedList([1,2,3,4,5,6,7,8,9,10])
    k = 5
    cylic_right_shift_linked_list(ll, k)
    print(ll)


if __name__ == "__main__":
    main()
