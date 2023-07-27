from linked_list import LinkedList
from reverse_sublist import reverse_a_sublist
from overlapping_linked_list_w_cycle import advance_node_by_steps

def linked_list_palindrome(ll: LinkedList):
    if not ll.head or not ll.head.next:
        return True
    linked_list_length = len(ll)
    reversal_start = linked_list_length // 2 + 1 + linked_list_length % 2
    reverse_a_sublist(ll, reversal_start, linked_list_length)
    advanced_node = advance_node_by_steps(ll.head, reversal_start - 1)
    curr_node = ll.head
    while curr_node and advanced_node and advanced_node.val == curr_node.val:
        advanced_node = advanced_node.next
        curr_node = curr_node.next
    reverse_a_sublist(ll, reversal_start, linked_list_length)
    return advanced_node is None

def main():
    ll = LinkedList([1,2,5,2,1])
    print(linked_list_palindrome(ll))


if __name__ == "__main__":
    main()
