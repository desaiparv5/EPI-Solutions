from collections import namedtuple
from typing import Optional
from binary_search_tree import BinarySearchTree, BinaryTreeNode


Interval = namedtuple("Interval", ("left", "right"))

def range_in_bst_tree(tree: BinarySearchTree, interval: Interval):
    nodes = []
    def helper(root: Optional[BinaryTreeNode]):
        if not root:
            return None
        if interval.left <= root.value <= interval.right:
            helper(root.left)
            nodes.append(root)
            helper(root.right)
        elif root.value < interval.left:
            helper(root.right)
        else:
            helper(root.left)
    helper(tree.root)
    return nodes


def main():
    tree = BinarySearchTree()
    interval = Interval(4, 10)
    tree.insert(8)
    tree.insert(4)
    tree.insert(11)
    tree.insert(21)
    tree.insert(5)
    tree.insert(0)
    tree.insert(3)
    tree.insert(9)
    tree.insert(2)
    print(range_in_bst_tree(tree, interval))


if __name__ == "__main__":
    main()
