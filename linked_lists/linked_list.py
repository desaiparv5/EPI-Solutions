import typing


class Node:
    def __init__(self, val, next: typing.Union[None, "Node"]=None, prev: typing.Union[None, "Node"]=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.val}"
    
    def __str__(self) -> str:
        return self.__repr__()


class LinkedList:
    def __init__(self, values = []) -> None:
        self.head = None
        self.tail = None

        for value in values:
            self.add_tail(value)

    def add_tail(self, val: typing.Any) -> None:
        if not self.head and not self.tail:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            assert self.tail
            self.tail = self.tail.next

    def add_head(self, val: typing.Any) -> None:
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            self.head = Node(val, next=self.head)

    def __len__(self) -> int:
        count = 0
        for _ in self:
            count += 1
        return count

    def __repr__(self) -> str:
        return " -> ".join([str(node) for node in self])

    def __iter__(self) -> typing.Generator["Node", None, None]:
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
    
    def find_node(self, val: typing.Any) -> typing.Union[None, Node]:
        assert self.head
        if self.head.val == val:
            return self.head
        curr_node = self.head.next
        while curr_node and curr_node.val != val and curr_node != self.head:
            curr_node = curr_node.next
        
        return None if curr_node == self.head else curr_node
    
    def empty_list(self) -> None:
        self.tail = self.head = None

    def delete_head(self) -> None:
        if self.head == self.tail:
            self.empty_list()
        else:
            assert self.head
            self.head = self.head.next

    def delete_tail(self) -> None:
        if self.head == self.tail:
            self.empty_list()
        curr_node = self.head
        while curr_node and curr_node.next != self.tail:
            curr_node = curr_node.next
        self.tail = curr_node
        assert self.tail
        self.tail.next = None

    def delete_next_node(self, node: Node) -> None:
        if node == self.tail:
            self.delete_tail()
        if node.next == self.tail:
            self.tail = node
        assert node and node.next
        node.next = node.next.next

    def delete_node(self, node: Node) -> None:
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        else:
            curr_node = self.head

            while curr_node and curr_node.next != node and curr_node.next != self.tail:
                curr_node = curr_node.next
            assert curr_node
            if curr_node.next == node:
                self.delete_next_node(curr_node)
    
    def update_tail(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        self.tail = curr


class DoublyLinkedList(LinkedList):
    def add_head(self, value: typing.Any) -> None:
        if not self.head and not self.tail:
            self.head = self.tail = Node(value)
            return
        self.head.prev = Node(value, next=self.head)
        self.head = self.head.prev

    def add_tail(self, value: typing.Any) -> None:
        if not self.head and not self.tail:
            self.head = self.tail = Node(value)
            return
        self.tail.next = Node(value, prev=self.tail)
        self.tail = self.tail.next
    
    def delete_tail(self):
        raise NotImplementedError

    def delete_head(self, *args, **kwargs):
        raise NotImplementedError

    def delete_next_node(self, node: Node) -> None:
        super().delete_next_node(node)
        assert node.next
        node.next.prev = node
