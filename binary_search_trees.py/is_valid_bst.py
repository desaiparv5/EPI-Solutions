from typing import Optional
from binary_trees.binary_tree import BinaryTree, BinaryTreeNode
from binary_trees.reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def is_valid_bst(tree: BinaryTree) -> bool:
    def valid_bst_helper(root: Optional[BinaryTreeNode], left: Optional[BinaryTreeNode], right: Optional[BinaryTreeNode]) -> bool:
        if not root:
            return True
        if left and left >= root:
            return False
        if right and right <= root:
            return False
        return valid_bst_helper(root.left, left, root) and valid_bst_helper(root.right, root, right)
    return valid_bst_helper(tree.root, None, None)


def main():
    node0 = BinaryTreeNode(0)
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(3)
    preorder_traversal = [node3, node1, node0, node2, node7, node5, node4, node6]
    inorder_traversal = [node0, node1, node2, node7, node3, node4, node5, node6]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(is_valid_bst(tree))


if __name__ == "__main__":
    main()
