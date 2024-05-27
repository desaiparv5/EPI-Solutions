from binary_trees.binary_tree import BinaryTreeNode


def generate_binary_trees(n):
    def helper(num_nodes):
        if num_nodes == 0:
            return [None]
        res = []
        for left_nodes in range(num_nodes):
            right_nodes = num_nodes - left_nodes - 1
            left_subtree = helper(left_nodes)
            right_subtree = helper(right_nodes)
            res += [
                BinaryTreeNode(0, left, right)
                for left in left_subtree
                for right in right_subtree
            ]
        return res
    return helper(n)


def main():
    print(generate_binary_trees(3))


if __name__ == "__main__":
    main()
