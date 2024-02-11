from typing import List
from binary_search_tree import BinarySearchTree


class ABRoot2:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.value = a + b * (2 ** (1 / 2))
    
    def __le__(self, obj: "ABRoot2") -> bool:
        return self.value < obj.value

    def __gt__(self, obj: "ABRoot2") -> bool:
        return self.value > obj.value
    
    def __repr__(self) -> str:
        return f"{self.a} + {self.b}root2"


def enumerate_abroot2(k: int) -> List[ABRoot2]:
    if k == 0:
        return []
    
    bst = BinarySearchTree()
    bst.add(ABRoot2(0, 0))
    res = []
    while len(res) < k:
        min_node = bst.get_minimum()
        bst.root = bst.delete_node(bst.root, min_node)  # type: ignore
        ab_root = min_node.value
        res.append(ab_root)
        bst.add(ABRoot2(ab_root.a + 1, ab_root.b))
        bst.add(ABRoot2(ab_root.a, ab_root.b + 1))
    return res


def main():
    k = 6
    print(enumerate_abroot2(k))


if __name__ == "__main__":
    main()
