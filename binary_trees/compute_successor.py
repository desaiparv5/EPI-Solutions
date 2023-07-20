from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal
from stacks_and_queues.stack_and_queue import Stack

# DOES NOT WORK FOR LAST NODE IN INORDER
def find_path_to_node(tree: BinaryTree, node: BinaryTreeNode):
    stack = Stack()

    def helper(root: BinaryTreeNode):
        if not root:
            return False
        stack.push(root)
        if root == node:
            return True

        if helper(root.left) or helper(root.right):
            return True
        stack.pop()

    if tree.root:
        helper(tree.root)

    return list(stack)


def compute_successor(tree: BinaryTree, node: BinaryTreeNode):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        path = find_path_to_node(tree, node)
    
    if len(path) < 1:
        return None
    for node in path[-2::-1]:
        if node.left:
            return node


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

    print(compute_successor(tree, node5))


if __name__ == "__main__":
    main()
