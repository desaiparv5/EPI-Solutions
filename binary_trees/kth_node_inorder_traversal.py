from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal
from stacks_and_queues.stack_and_queue import Stack


def kth_node_inorder_traversal(tree: BinaryTree, k):
    count = 0
    curr_node = tree.root
    stack = Stack([curr_node])
    while curr_node and count < k:
        if curr_node.left:
            stack.push(curr_node.left)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            count += 1
            if count == k:
                return curr_node
            if curr_node and curr_node.right:
                stack.push(curr_node.right)
                curr_node = curr_node.right
    return curr_node


def main():
    node1 = BinaryTreeNode(5)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(1)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(6)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(8)
    preorder_traversal = [node1, node2, node3, node4, node5, node6, node7]
    inorder_traversal = [node3, node2, node4, node1, node6, node5, node7]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)

    k = 4
    print(kth_node_inorder_traversal(tree, k))


if __name__ == "__main__":
    main()
