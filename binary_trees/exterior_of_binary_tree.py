from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_tree_w_markers import reconstruct_binary_tree_from_postorder_w_markers


def leftmost_nodes(tree: BinaryTree):
    nodes = []
    def _helper(root: BinaryTreeNode):
        if not root:
            return
        nodes.append(root)
        _helper(root.left)
    if tree.root:
        nodes.append(tree.root)
        _helper(tree.root.left)
    return nodes


def rightmost_nodes(tree: BinaryTree):
    nodes = []
    def _helper(root: BinaryTreeNode):
        if not root:
            return
        nodes.append(root)
        _helper(root.right)
    if tree.root:
        nodes.append(tree.root)
        _helper(tree.root.right)
    return nodes


def leaves_of_tree(tree: BinaryTree):
    nodes = []
    def _helper(root: BinaryTreeNode):
        if not root:
            return
        if not root.left and not root.right:
            nodes.append(root)
        _helper(root.left)
        _helper(root.right)
    if tree._root:
        _helper(tree.root)
    return nodes


def exterior_of_binary_tree(tree: BinaryTree):
    return leftmost_nodes(tree)[:-1] + leaves_of_tree(tree) + rightmost_nodes(tree)[1:-1]


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(4)
    node4 = BinaryTreeNode(5)
    node5 = BinaryTreeNode(3)
    postorder_traversal = [None, None, node3, None, None, node4, node2, None, None, node5, node1]
    tree = reconstruct_binary_tree_from_postorder_w_markers(postorder_traversal)
    print(exterior_of_binary_tree(tree))


if __name__ == "__main__":
    main()
