import typing


class BinaryTreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self._val = val
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def value(self):
        return self._val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent
    
    @right.setter
    def right(self, node: "BinaryTreeNode"):
        self._right = node
        if node:
            node.parent = self

    @left.setter
    def left(self, node: "BinaryTreeNode"):
        self._left = node
        if node:
            node.parent = self
    
    @parent.setter
    def parent(self, node: "BinaryTreeNode"):
        self._parent = node
    
    def __repr__(self) -> str:
        return f"{self.value}"
    
    def __float__(self) -> float:
        return float(self.value)


class BinaryTree:
    def __init__(self, preorder_values=None):
        self._root: BinaryTreeNode = None # type: ignore
        if preorder_values:
            self._create_tree_from_preorder_values(preorder_values)
    
    @property
    def root(self) -> typing.Union[None, BinaryTreeNode]:
        return self._root
    
    @root.setter
    def root(self, obj: typing.Union[BinaryTreeNode, None]):
        self._root = obj # type: ignore
    
    def __bool__(self):
        return self.root is not None

    def height(self):
        def _height(root: typing.Union[None, BinaryTreeNode]):
            if not root:
                return 0
            return 1 + max(_height(root.left), _height(root.right))

        if not self._root:
            return None
        else:
            return _height(self._root)   

    def add(self, val):
        def _add(val, root: BinaryTreeNode):
            if val > root.value:
                if root.right:
                    _add(val, root.right)
                else:
                    root.right = BinaryTreeNode(val=val, parent=root)
            elif val <= root.value:
                if root.left:
                    _add(val, root.left)
                else:
                    root.left = BinaryTreeNode(val, parent=root)

        if not self._root:
            self._root = BinaryTreeNode(val)
        else:
            _add(val, self._root)


    def inorder_traversal(self):
        inorder_list = []
        def _inorder_traversal(root: typing.Union[None, BinaryTreeNode]):
            if not root:
                return None
            else:
                _inorder_traversal(root.left)
                inorder_list.append(root)
                _inorder_traversal(root.right)
        if not self._root:
            return []
        _inorder_traversal(self._root)
        return inorder_list

    def preorder_traversal(self):
        preorder_list = []
        def _preorder_traversal(root: typing.Union[None, BinaryTreeNode]):
            if not root:
                return None
            else:
                preorder_list.append(root)
                _preorder_traversal(root.left)
                _preorder_traversal(root.right)
        if not self._root:
            return []
        _preorder_traversal(self._root)
        return preorder_list

    def postorder_traversal(self):
        postorder_list = []
        def _postorder_traversal(root: typing.Union[None, BinaryTreeNode]):
            if not root:
                return None
            else:
                _postorder_traversal(root.left)
                _postorder_traversal(root.right)
                postorder_list.append(root)
        if not self._root:
            return None
        _postorder_traversal(self._root)
        return postorder_list
