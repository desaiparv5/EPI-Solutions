from binary_tree import BinaryTreeNode, BinaryTree
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


class BinaryTreeNodeSibling(BinaryTreeNode):
    def __init__(self, val, left=None, right=None, parent=None):
        super().__init__(val, left, right, parent)
        self._next = None
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, _obj: "BinaryTreeNodeSibling"):
        self._next = _obj
        

def right_sibling_tree(tree: BinaryTree):
    pass


def main():
    node1 = BinaryTreeNode(5)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(1)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(6)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(8)
    preorder_traversal = [node1, node2, node3, node4, node5, node6, node7]
    inorder_traversal = [node3, node2, node4, node1, node6, node5, node7]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)

    right_sibling_tree(tree)
    print(tree.inorder_traversal())


if __name__ == "__main__":
    main()
