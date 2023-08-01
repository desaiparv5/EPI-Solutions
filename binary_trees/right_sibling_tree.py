from binary_tree import BinaryTreeNode, BinaryTree
from reconstruct_binary_tree import reconstruct_binary_tree_from_preorder_inorder_traversal
from stacks_and_queues.stack_and_queue import Queue


class BinaryTreeNodeSibling(BinaryTreeNode):
    def __init__(self, val, left=None, right=None, parent=None):
        super().__init__(val, left, right, parent)
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _obj: "BinaryTreeNodeSibling"):
        self._next = _obj


def right_sibling_tree(tree: BinaryTree):
    if not tree.root:
        return
    queue = Queue(values=[tree.root])
    while queue:
        size = len(queue)
        prev = None
        for _ in range(size):
            node = queue.dequeue()
            node.next = prev
            prev = node
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)


def main():
    node1 = BinaryTreeNodeSibling(5)
    node2 = BinaryTreeNodeSibling(1)
    node3 = BinaryTreeNodeSibling(1)
    node4 = BinaryTreeNodeSibling(4)
    node5 = BinaryTreeNodeSibling(6)
    node6 = BinaryTreeNodeSibling(6)
    node7 = BinaryTreeNodeSibling(8)
    preorder_traversal = [node1, node2, node3, node4, node5, node6, node7]
    inorder_traversal = [node3, node2, node4, node1, node6, node5, node7]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)

    right_sibling_tree(tree)


if __name__ == "__main__":
    main()

"""
      5
  1       6
1   4   6   8
"""