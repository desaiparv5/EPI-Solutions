from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def sum_root_to_leaf(tree: BinaryTree):
    def _helper(node: BinaryTreeNode, partial_sum):
        partial_sum = partial_sum * 2 + node.value
        if not node.left and not node.right:
            return partial_sum
        left_sum = _helper(node.left, partial_sum) if node.left else 0
        right_sum = _helper(node.right, partial_sum) if node.right else 0
        return left_sum + right_sum
    if not tree.root:
        return 0
    return _helper(tree.root, 0)


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(1)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(sum_root_to_leaf(tree))


if __name__ == "__main__":
    main()
