from typing import List
from binary_search_tree import BinarySearchTree, BinaryTreeNode


def reconstruct_bst_from_preorder(preorder_sequence: List[int]) -> BinarySearchTree:
    root_index = [0]
    def reconstruct_bst_helper(lower_bound, upper_bound) -> BinaryTreeNode:
        if root_index[0] >= len(preorder_sequence):
            return None  # type: ignore
        if preorder_sequence[root_index[0]] < lower_bound or preorder_sequence[root_index[0]] > upper_bound:
            return None  # type: ignore
        node = BinaryTreeNode(preorder_sequence[root_index[0]])
        root_index[0] += 1
        node.left = reconstruct_bst_helper(lower_bound, node.value)
        node.right = reconstruct_bst_helper(node.value, upper_bound)
        return node
    tree = BinarySearchTree()
    tree.root = reconstruct_bst_helper(float("-inf"), float("inf"))
    return tree


def main():
    preorder_sequence = [7, 2, 1, 4, 5, 8, 10]
    tree = reconstruct_bst_from_preorder(preorder_sequence)
    print(tree.preorder_traversal())


if __name__ == "__main__":
    main()
