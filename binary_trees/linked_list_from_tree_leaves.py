from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_tree_w_markers import reconstruct_binary_tree_from_postorder_w_markers
from linked_lists.linked_list import LinkedList


def linked_list_from_tree_leaves(tree: BinaryTree) -> LinkedList:
    if not tree.root:
        return None
    ll = LinkedList()
    def _helper(root: BinaryTreeNode):
        if root.left:
            _helper(root.left)
        if root.right:
            _helper(root.right)
        if not root.left and not root.right:
            ll.add_tail(root)
            return

    _helper(tree.root)
    return ll


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(4)
    node4 = BinaryTreeNode(5)
    node5 = BinaryTreeNode(3)
    postorder_traversal = [None, None, node3, None, None, node4, node2, None, None, node5, node1]
    tree = reconstruct_binary_tree_from_postorder_w_markers(postorder_traversal)
    ll = linked_list_from_tree_leaves(tree)
    print(ll) 

if __name__ == "__main__":
    main()
