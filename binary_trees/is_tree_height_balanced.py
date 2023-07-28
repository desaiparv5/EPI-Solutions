from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal
from collections import namedtuple


def is_tree_height_balanced(tree: BinaryTree):
    if not tree.root:
        return False

    BalancedStatus = namedtuple("BalanceStatus", ("status", "height"))
    def _helper(root: BinaryTreeNode) -> BalancedStatus:
        if root.left:
            left_result = _helper(root.left)
            if not left_result.status:
                return BalancedStatus(False, 0)
        else:
            left_result = BalancedStatus(True, 0)
        
        if root.right:
            right_result = _helper(root.right)
            if not right_result.status:
                return BalancedStatus(False, 0)
        else:
            right_result = BalancedStatus(True, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatus(is_balanced, height)

    return _helper(tree.root).status

def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    preorder_traversal = [node1, node2, node3]
    inorder_traversal = [node1, node2, node3]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(is_tree_height_balanced(tree))


if __name__ == "__main__":
    main()
