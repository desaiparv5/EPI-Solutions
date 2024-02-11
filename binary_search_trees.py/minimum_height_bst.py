from typing import List
from binary_search_tree import BinarySearchTree, BinaryTreeNode


def minimum_height_bst(arr: List[int]) -> BinarySearchTree:
    def helper(start, end):
        if start > end:
            return
        mid = (start + end) // 2
        return BinaryTreeNode(left=helper(start, mid - 1), right=helper(mid + 1, end), val=arr[mid])
    tree = BinarySearchTree()
    tree.root = helper(0, len(arr) - 1)  # type: ignore
    return tree


def main():
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    tree = minimum_height_bst(arr)
    print(tree.inorder_traversal())


if __name__ == "__main__":
    main()
