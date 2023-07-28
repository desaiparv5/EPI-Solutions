import typing
from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def get_depth(node: BinaryTreeNode):
    count = 0
    while node.parent:
        node = node.parent
        count += 1
    return count


def lowest_common_ancestor_w_parent(tree: BinaryTree, node1: BinaryTreeNode, node2: BinaryTreeNode):
    if not tree.root:
        return None

    depth1 = get_depth(node1)
    depth2 = get_depth(node2)

    if depth1 < depth2:
        node1, node2 = node2, node1
    
    for _ in range(abs(depth1 - depth2)):
        assert node1.parent
        node1 = node1.parent
    
    while node1 and node2 and node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    print(lowest_common_ancestor_w_parent(tree, node2, node3))


if __name__ == "__main__":
    main()
