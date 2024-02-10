from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def is_tree_symmetric(tree: BinaryTree):
    if not tree.root:
        return False
    def _helper(root: BinaryTreeNode):
        if not (root.left or root.right):
            return True
        elif not (root.left and root.right) or root.left != root.right:
            return False
        else:
            return _helper(root.left) and _helper(root.right)
    return _helper(tree.root)


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(2)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(is_tree_symmetric(tree))


if __name__ == "__main__":
    main()
