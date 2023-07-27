import typing
from linked_list import LinkedList


def delete_node_from_single_linked_list(ll: LinkedList, val: typing.Any) -> None:
    node = ll.find_node(val)
    _ = node and ll.delete_node(node)


def main():
    ll = LinkedList([1,2,3,4,5,6,7,8])
    delete_node_from_single_linked_list(ll, 8)
    print(ll)
    delete_node_from_single_linked_list(ll, 2)
    print(ll)
    delete_node_from_single_linked_list(ll, 1)
    print(ll)


if __name__ == "__main__":
    main()
