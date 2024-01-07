from typing import Optional, Union
from linked_lists.linked_list import LinkedList, Node


def sort_linked_list(ll: LinkedList):
    def merge(node1: Optional[Node]=None, node2:Optional[Node]=None):
        dummy = Node(0)
        curr = dummy

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next

        if node1:
            curr.next = node1
        if node2:
            curr.next = node2
        return dummy.next

    def sort_linked_list_helper(node: Optional[Node] = None) -> Union[Node, None]:
        if not node or not node.next:
            return node
        
        slow, fast = node, node.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = sort_linked_list_helper(node)
        right = sort_linked_list_helper(mid)

        res = merge(left, right)
        return res

    if not ll.head:
        return
    ll.head = sort_linked_list_helper(ll.head)
    ll.update_tail()



def main():
    ll = LinkedList([4,1,3,2,7,5,6])
    sort_linked_list(ll)
    print(ll)


if __name__ == "__main__":
    main()
