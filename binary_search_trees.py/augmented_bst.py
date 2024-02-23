import random
from typing import Optional, Tuple
from binary_search_tree import BinarySearchTree, BinaryTreeNode


class AugmentedBSTNode(BinaryTreeNode):
    def __init__(self, val, left=None, right=None, parent=None):
        super().__init__(val, left, right, parent)
        self.left_tree_size = 0
        self.right_tree_size = 0
        self.left: "AugmentedBSTNode"
        self.right: "AugmentedBSTNode"
        self.parent: "AugmentedBSTNode"


class AugmentedBST(BinarySearchTree):
    def __init__(self) -> None:
        self.root: AugmentedBSTNode = None  # type: ignore
    
    def insert(self, val: int) -> None:
        self.root = self.insert_node(self.root, AugmentedBSTNode(val))
    
    @classmethod
    def insert_node(cls, root: Optional[AugmentedBSTNode], node: AugmentedBSTNode) -> AugmentedBSTNode:
        if not root:
            return node
        if node < root:
            root.left_tree_size += 1
            root.left = cls.insert_node(root.left, node)
        else:
            root.right_tree_size += 1
            root.right = cls.insert_node(root.right, node)
        return root
    
    def delete(self, key):
        node = AugmentedBSTNode(key)
        self.root, _ = self.delete_node(self.root, node)  # type: ignore

    
    @classmethod
    def delete_node(cls, root: Optional[AugmentedBSTNode], node: AugmentedBSTNode) -> Tuple[AugmentedBSTNode, bool]:
        if not root:
            return None, False  # type: ignore
        if node < root:
            root.left, node_found = cls.delete_node(root.left, node)
            root.left_tree_size -= (1 if node_found else 0)
        elif node > root:
            root.right, node_found = cls.delete_node(root.right, node)
            root.right_tree_size -= (1 if node_found else 0)
        else:
            if not root.left and not root.right:
                return None, True  # type: ignore
            if not root.left:
                return root.right, True
            if not root.right:
                return root.left, True
            leftmost_right_node: AugmentedBSTNode = cls.smallest_node(root.right)  # type: ignore
            root.value = leftmost_right_node.value
            root.right, _ = cls.delete_node(root.right, leftmost_right_node)
            root.right_tree_size -= 1
        return root, True

    def num_node_less_than(self, k):
        def helper(root: AugmentedBSTNode):
            if not root:
                return 0
            if root.value > k:
                return helper(root.left)
            if root.value <= k:
                return root.left_tree_size + helper(root.right) + 1
        return helper(self.root)

    def num_node_greater_than(self, k):
        def helper(root: AugmentedBSTNode):
            if not root:
                return 0
            if root.value < k:
                return helper(root.right)
            if root.value >= k:
                return root.right_tree_size + helper(root.left) + 1
        return helper(self.root)

    def num_nodes_in_range(self, a, b):
        pass

    
bst = AugmentedBST()

for i in range(30):
    bst.insert(random.randint(0, 100))

print(bst.inorder_traversal())
