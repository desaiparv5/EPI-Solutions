from binary_trees.binary_tree import BinaryTree, BinaryTreeNode
from binary_trees.reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def lowest_common_ancestor(tree: BinaryTree, node1: BinaryTreeNode, node2: BinaryTreeNode):
    iter1, iter2 = node1, node2
    visited_nodes = set()
    while iter1 or iter2:
        if iter1:
            if iter1 in visited_nodes:
                return iter1
            visited_nodes.add(iter1)
            iter1 = iter1.parent
        if iter2:
            if iter2 in visited_nodes:
                return iter2
            visited_nodes.add(iter2)
            iter2 = iter2.parent
    return None



def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(lowest_common_ancestor(tree, node2, node3))


if __name__ == "__main__":
    main()
