import typing
from binary_trees.binary_tree import BinaryTree, BinaryTreeNode
from stack_and_queue import Queue


def compute_tree_nodes_in_depth_order(tree: BinaryTree) -> typing.List[typing.List]:
    queue = Queue()
    res = []
    if tree:
        queue.enqueue(tree.root)
    
    while queue:
        temp_arr = []
        for _ in range(len(queue)):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            temp_arr.append(node)
        res.append(temp_arr)
    return res


def compute_tree_nodes_depth_alternating_order(tree: BinaryTree):
    queue = Queue()
    res = []
    if tree:
        queue.enqueue(tree.root)
    
    while queue:
        temp_arr = []
        for _ in range(len(queue)):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            temp_arr.append(node)
        if len(res) % 2:
            res.append(temp_arr[::-1])
        else:
            res.append(temp_arr)
    return res


def compute_tree_nodes_depth_bottom_up(tree: BinaryTree):
    return compute_tree_nodes_in_depth_order(tree)[::-1]


def compute_average_of_each_level(tree: BinaryTree):
    queue = Queue()
    res = []
    if tree:
        queue.enqueue(tree.root)
    
    while queue:
        temp_arr = []
        for _ in range(len(queue)):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            temp_arr.append(float(node))
        res.append(sum(temp_arr) / len(temp_arr))
    return res


def main():
    tree = BinaryTree()
    tree.add(5)
    tree.add(1)
    tree.add(6)
    tree.add(9)
    tree.add(8)
    tree.add(2)
    tree.add(1)
    tree.add(0)
    print(compute_tree_nodes_in_depth_order(tree))
    print(compute_tree_nodes_depth_alternating_order(tree))
    print(compute_tree_nodes_depth_bottom_up(tree))
    print(compute_average_of_each_level(tree))


if __name__ == "__main__":
    main()
