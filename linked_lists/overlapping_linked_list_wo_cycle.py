from linked_list import LinkedList, Node

def advance_node_by_steps(node: Node, steps: int) -> Node:
    for _ in range(steps):
        assert node
        node = node.next # type: ignore
    return node


def find_common_node(node1: Node, node2: Node) -> Node:
    while node1 and node2 and node1 is not node2:
        node1, node2 = node1.next, node2.next # type: ignore
    return node1


def are_linked_lists_overlapping(ll1: LinkedList, ll2: LinkedList):
    len1 = len(ll1)
    len2 = len(ll2)

    if len1 > len2:
        node1 = ll1.head
        node2 = ll2.head
    else:
        node1 = ll2.head
        node2 = ll1.head
    
    node1 = advance_node_by_steps(node1, abs(len1-len2)) # type: ignore
    return find_common_node(node1, node2) # type: ignore


def overlap_linked_list(ll1: LinkedList, ll2: LinkedList, ind: int) -> None:
    curr_node = ll1.head
    for _ in range(ind):
        assert curr_node
        curr_node = curr_node.next
    assert ll2.tail
    ll2.tail.next = curr_node


def main():
    ll1 = LinkedList([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    ll2 = LinkedList([1, 2, 3])
    overlap_linked_list(ll1, ll2, 4)
    print(are_linked_lists_overlapping(ll1, ll2))


if __name__ == "__main__":
    main()

