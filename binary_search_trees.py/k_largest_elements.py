from typing import List, Optional
from binary_search_tree import BinarySearchTree, BinaryTreeNode


def k_largest_elements(tree: BinarySearchTree, k: int) -> List[BinaryTreeNode]:
    k_largest_elements = []
    def k_largest_element_helper(root: Optional[BinaryTreeNode]):
        if root and len(k_largest_elements) < k:
            k_largest_element_helper(root.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(root)
                k_largest_element_helper(root.left)

    k_largest_element_helper(tree.root)
    return k_largest_elements


def main():
    tree = BinarySearchTree()
    tree.add(7)
    tree.add(2)
    tree.add(8)
    tree.add(10)
    tree.add(4)
    tree.add(1)
    tree.add(5)
    k = 5
    print(k_largest_elements(tree, k))


if __name__ == "__main__":
    main()
