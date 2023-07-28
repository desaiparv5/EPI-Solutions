from binary_tree import BinaryTree, BinaryTreeNode
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal
from stacks_and_queues.stack_and_queue import Queue
from copy import deepcopy


def path_to_sum(tree: BinaryTree, target_sum):
    if not tree.root:
        return []
    all_paths = Queue()
    def _helper(node: BinaryTreeNode, partial_sum: int, curr_path: Queue):
        partial_sum += node.value
        curr_path.enqueue(node)
        if not node.left and not node.right:
            _ = partial_sum == target_sum and all_paths.enqueue(deepcopy(curr_path))
        if node.left:
            _helper(node.left, partial_sum, curr_path)
        if node.right:
            _helper(node.right, partial_sum, curr_path)
        curr_path.dequeue()
    _helper(tree.root, 0, Queue())
    return [path for path in all_paths]


def main():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(1)
    preorder_traversal = [node1, node3, node2]
    inorder_traversal = [node3, node1, node2]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    target_sum = 3
    print(path_to_sum(tree, target_sum))


if __name__ == "__main__":
    main()
