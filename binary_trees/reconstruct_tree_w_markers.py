from binary_tree import BinaryTreeNode, BinaryTree
import typing


def node_iterator(traversal):
    for node in traversal:
        yield node

def reconstruct_binary_tree_from_preorder_w_markers(preorder_traversal: typing.List[BinaryTreeNode]) -> BinaryTree:
    tree = BinaryTree()
    if not preorder_traversal:
        return None # type: ignore
    _iter = node_iterator(preorder_traversal)

    def _helper():
        try:
            node = next(_iter)
            if  node is None:
                return None
            node.left = _helper() # type: ignore
            node.right = _helper() # type: ignore
            return node
        except StopIteration:
            return None

    tree.root = _helper()
    return tree


def reconstruct_binary_tree_from_postorder_w_markers(postorder_traversal: typing.List[BinaryTreeNode]) -> BinaryTree:
    tree = BinaryTree()
    if not postorder_traversal:
        return None # type: ignore
    _iter = node_iterator(postorder_traversal[::-1])

    def _helper():
        try:
            node = next(_iter)
            if  node is None:
                return None
            node.right = _helper() # type: ignore
            node.left = _helper() # type: ignore
            return node
        except StopIteration:
            return None

    tree.root = _helper()
    return tree


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(4)
    node4 = BinaryTreeNode(5)
    node5 = BinaryTreeNode(3)
    preorder_traversal = [node1, node2, node3, None, None, node4, None, None, node5, None, None]
    tree = reconstruct_binary_tree_from_preorder_w_markers(preorder_traversal)
    postorder_traversal = [None, None, node3, None, None, node4, node2, None, None, node5, node1]
    tree = reconstruct_binary_tree_from_postorder_w_markers(postorder_traversal)
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())


if __name__ == "__main__":
    main()
