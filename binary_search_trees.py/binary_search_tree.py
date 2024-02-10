from typing import Any, Optional, Union
from binary_trees.binary_tree import BinaryTreeNode, BinaryTree

class BinarySearchTree(BinaryTree):
    def __init__(self) -> None:
        self.root: BinaryTreeNode = None  # type: ignore

    @classmethod
    def smallest_node(cls, root: Optional[BinaryTreeNode]) -> Union[None, BinaryTreeNode]:
        if not root:
            return None
        while root.left:
            root = root.left
        return root

    def smallest(self) -> Union[None, BinaryTreeNode]:
        return self.largest_node(self.root)

    @classmethod
    def largest_node(cls, root: Optional[BinaryTreeNode]) -> Union[None, BinaryTreeNode]:
        if not root:
            return None
        while root.right:
            root = root.right
        return root

    def largest(self) -> Union[None, BinaryTreeNode]:
        return self.largest_node(self.root)

    @classmethod
    def search_node(cls, root: Optional[BinaryTreeNode], node: BinaryTreeNode) -> Union[None, BinaryTreeNode]:
        if not root:
            return None
        if root == node:
            return root
        if root < root:
            return cls.search_node(root.left, node)
        return cls.search_node(root.right, node)

    def search(self, node: BinaryTreeNode) -> Union[None, BinaryTreeNode]:
        return self.search_node(self.root, node)

    @classmethod
    def insert_node(cls, root: Optional[BinaryTreeNode], node: BinaryTreeNode) -> BinaryTreeNode:
        if not root:
            return node
        if node < root:
            root.left = cls.insert_node(root.left, node)
        else:
            root.right = cls.insert_node(root.right, node)
        return root

    def insert(self, val: int) -> None:
        self.root = self.insert_node(self.root, BinaryTreeNode(val))

    @classmethod
    def delete_node(cls, root: Optional[BinaryTreeNode], node: BinaryTreeNode) -> Union[None, BinaryTreeNode]:
        if not root:
            return None
        if node < root:
            root.left = cls.delete_node(root.left, node)
        elif node > root:
            root.right = cls.delete_node(root.right, node)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            leftmost_right_node = cls.smallest_node(root.right)
            root.value = leftmost_right_node.value
            root.right = cls.delete_node(root.right, leftmost_right_node)
        return root

    def delete(self, key):
        node = BinaryTreeNode(key)
        self.root = self.delete_node(self.root, node)  # type: ignore
