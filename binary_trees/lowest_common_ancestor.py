import typing
from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def lowest_common_ancestor(tree: BinaryTree, nodes: typing.List[BinaryTreeNode]):
    if not tree.root:
        return None

    def _helper(root: BinaryTreeNode, nodes):
        if root in nodes:
            return root
        if root.left:
            left_ancestor = _helper(root.left, nodes)
        else:
            return None

        if root.right:
            right_ancestor = _helper(root.right, nodes)
        else:
            return None
        
        if left_ancestor and right_ancestor:
            return root
        
        return left_ancestor or right_ancestor
    
    return _helper(tree.root, nodes)


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(lowest_common_ancestor(tree, [node2, node3]))


if __name__ == "__main__":
    main()
