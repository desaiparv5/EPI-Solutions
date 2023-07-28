from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal


def inorder_using_constant_space(tree: BinaryTree):
    # Morris traversal
    out_list = []
    curr_node = tree.root
    while curr_node:
        if not curr_node.left:
            out_list.append(curr_node)
            curr_node = curr_node.right
        else:
            left_subtree = curr_node.left
            while left_subtree.right and left_subtree.right != curr_node:
                left_subtree = left_subtree.right
            
            if left_subtree.right == curr_node:
                left_subtree.right = None # type: ignore
                out_list.append(curr_node)
                curr_node = curr_node.right
            else:
                left_subtree.right = curr_node
                curr_node = curr_node.left
    return out_list


def preorder_using_constant_space(tree: BinaryTree):
    # Morris traversal
    out_list = []
    curr_node = tree.root
    while curr_node:
        if not curr_node.left:
            out_list.append(curr_node)
            curr_node = curr_node.right
        else:
            left_subtree = curr_node.left
            while left_subtree.right and left_subtree.right != curr_node:
                left_subtree = left_subtree.right

            if left_subtree.right == curr_node:
                left_subtree.right = None # type: ignore
                curr_node = curr_node.right
            else:
                out_list.append(curr_node)
                left_subtree.right = curr_node
                curr_node = curr_node.left
    return out_list


def postorder_using_constant_space(tree: BinaryTree):
    # Morris traversal
    out_list = []
    curr_node = tree.root
    while curr_node:
        if not curr_node.right:
            out_list.append(curr_node)
            curr_node = curr_node.left
        else:
            right_subtree = curr_node.right
            while right_subtree.left and right_subtree.left != curr_node:
                right_subtree = right_subtree.left

            if right_subtree.left == curr_node:
                right_subtree.left = None # type: ignore
                curr_node = curr_node.left
            else:
                out_list.append(curr_node)
                right_subtree.left = curr_node
                curr_node = curr_node.left
    out_list.reverse()
    return out_list


def main():
    node1 = BinaryTreeNode(5)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(1)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(6)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(8)
    preorder_traversal = [node1, node2, node3, node4, node5, node6, node7]
    inorder_traversal = [node7, node6, node5, node4, node3, node2, node1]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)

    inorder_traversal = inorder_using_constant_space(tree)
    print(inorder_traversal)
    preorder_traversal = preorder_using_constant_space(tree)
    print(preorder_traversal)
    postorder_traversal = postorder_using_constant_space(tree)
    print(postorder_traversal)


if __name__ == "__main__":
    main()
