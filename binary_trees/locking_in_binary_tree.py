from binary_tree import BinaryTreeNode


class BinaryTreeNodeLock(BinaryTreeNode):
    def __init__(self, val, left=None, right=None, parent=None):
        super().__init__(val, left, right, parent)
        self.num_lock = 0
        self._lock = False

    def is_locked(self):
        return self._lock

    def lock(self, node: "BinaryTreeNodeLock"):
        if self._lock or self.num_lock > 0:
            return False
        iter = node
        while iter:
            if iter.is_locked():
                return False
            iter = iter.parent
        iter = node
        while iter:
            iter.num_lock += 1
            iter = iter.parent
        return True

    def unlock(self, node: "BinaryTreeNodeLock"):
        if self.is_locked():
            self._lock = False
        iter = node
        while iter:
            iter.num_lock -= 1
            iter = iter.parent
