from binary_trees.binary_tree import BinaryTree, BinaryTreeNode


def get_diameter(tree: BinaryTree):
    ans = [0]
    def helper(node: BinaryTreeNode):
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        ans[0] = max(ans[0], left + right)
        return 1 + max(left, right)
    helper(tree.root)
    return ans[0]


def main():
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    print(get_diameter(tree))


if __name__ == "__main__":
    main()