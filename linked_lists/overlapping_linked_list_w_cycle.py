import typing
from linked_list import LinkedList, Node
from linked_list_cyclicity import linked_list_cyclicity, introduce_cycle_in_linked_list
from overlapping_linked_list_wo_cycle import are_linked_lists_overlapping, overlap_linked_list, advance_node_by_steps, find_common_node


def distance_between_nodes(start: Node, end: Node) -> int:
    count = 1
    while start is not end:
        assert start.next
        start = start.next
        count += 1
    return count


def part_of_same_cycle(root1: Node, root2: Node) -> bool:
    curr_node = root1.next
    while curr_node != root2 and curr_node != root1:
        assert curr_node
        curr_node = curr_node.next
    
    return curr_node == root2


def overlapping_linked_list_w_cycle(ll1: LinkedList, ll2: LinkedList) -> typing.Union[Node, None]:
    root1 = linked_list_cyclicity(ll1)
    root2 = linked_list_cyclicity(ll2)

    if bool(root1) ^ bool(root2):
        # only one Linked List contains a cycle
        return None

    if not (root1 or root2):
        # None of them have cycle
        return are_linked_lists_overlapping(ll1, ll2)
    
    if not part_of_same_cycle(root1, root2): # type: ignore
        # Both Linked List have different cycles
        return None

    len1 = distance_between_nodes(ll1.head, root1) # type: ignore
    len2 = distance_between_nodes(ll2.head, root2) # type: ignore

    if len1 > len2:
        node1 = ll1.head
        node2 = ll2.head
    else:
        node1 = ll2.head
        node2 = ll1.head

    assert node1
    node1 = advance_node_by_steps(node1, abs(len1-len2))
    
    while node1 != node2 or node1 != root1 or node1 != root2:
        assert node1 and node2
        node1 = node1.next
        node2 = node2.next
    
    return node1


def main():
    ll1 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ll2 = LinkedList([21, 22, 23, 24, 25, 26, 27])

    introduce_cycle_in_linked_list(ll1, 3)
    overlap_linked_list(ll1, ll2, 5)
    print(overlapping_linked_list_w_cycle(ll1, ll2))


if __name__ == "__main__":
    main()
