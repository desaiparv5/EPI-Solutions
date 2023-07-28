import typing
from binary_tree import BinaryTree, BinaryTreeNode


def find_node(nodes_list: typing.List[BinaryTreeNode], node: BinaryTreeNode, start_index: int, end_index: int) -> int:
        for i in range(start_index, end_index + 1):
            if nodes_list[i] == node:
                return i
        return -1

def reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal: typing.List[BinaryTreeNode], inorder_traversal: typing.List[BinaryTreeNode]):
    def _helper(preorder_index, inorder_start_index, inorder_end_index) -> typing.Union[BinaryTreeNode, None]:
        if preorder_index >= len(preorder_traversal) or inorder_start_index > inorder_end_index:
            return None
        root = preorder_traversal[preorder_index]
        inorder_index = find_node(inorder_traversal, root, inorder_start_index, inorder_end_index)
        if inorder_index == -1:
            raise Exception("Invalid traversal")
        root.left = _helper(preorder_index + 1, inorder_start_index, inorder_index - 1)
        preorder_right_index = preorder_index + inorder_index - inorder_start_index + 1
        root.right = _helper(preorder_right_index, inorder_index + 1, inorder_end_index)
        return root

    tree = BinaryTree()
    tree.root = _helper(0, 0, len(inorder_traversal) -1)
    return tree


def reconstruct_binary_tree_from_postorder_inorder_traversal(postorder_traversal: typing.List[BinaryTreeNode], inorder_traversal: typing.List[BinaryTreeNode]):
    def _helper(postorder_index, inorder_start_index, inorder_end_index) -> typing.Union[BinaryTreeNode, None]:
        if postorder_index < 0 or inorder_start_index > inorder_end_index:
            return None
        root = postorder_traversal[postorder_index]
        inorder_index = find_node(inorder_traversal, root, inorder_start_index, inorder_end_index)
        if inorder_index == -1:
            raise Exception("Invalid traversal")
        root.right = _helper(postorder_index - 1, inorder_index + 1, inorder_end_index)
        postorder_left_index = postorder_index - (inorder_end_index - inorder_index) - 1
        root.left = _helper(postorder_left_index, inorder_start_index, inorder_index - 1)
        return root

    tree = BinaryTree()
    tree.root = _helper(len(postorder_traversal) - 1, 0, len(inorder_traversal) -1)
    return tree


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
    postorder_traversal = [node3, node4, node2, node6, node7, node5, node1]
    tree = reconstruct_binary_tree_from_preorder_inorder_traversal(preorder_traversal, inorder_traversal)
    tree = reconstruct_binary_tree_from_postorder_inorder_traversal(postorder_traversal, inorder_traversal)
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())


if __name__ == "__main__":
    main()
