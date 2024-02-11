from typing import Optional
from binary_search_tree import BinarySearchTree, BinaryTreeNode


def first_key_greater_than_k(tree: BinarySearchTree, k: int) -> Optional[BinaryTreeNode]:
    node, first_so_far = tree.root, None
    while node:
        if node.value > k:
            node, first_so_far = node.left, node
        else:
            node = node.right
    return first_so_far


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
    print(first_key_greater_than_k(tree, k))


if __name__ == "__main__":
    main()
