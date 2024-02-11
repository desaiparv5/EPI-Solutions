from binary_search_tree import BinarySearchTree, BinaryTreeNode


def least_common_ancestor(tree: BinarySearchTree, node1: int, node2: int) -> BinaryTreeNode:
    lca = tree.root
    while lca:
        if node1 > lca.value and node2 > lca.value:
            lca = lca.right
        elif node1 < lca.value and node2 < lca.value:
            lca = lca.left
        else:
            break        
    return lca  # type: ignore

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
    node1 = 2
    node2 = 5
    print(least_common_ancestor(tree, node1, node2))


if __name__ == "__main__":
    main()
