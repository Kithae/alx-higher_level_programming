#!/usr/bin/python3
"""Define singly-linked list class."""


class Node:
    """ singly-linked list node representation."""

    def __init__(self, data, next_node=None):
        """new node initialization.
        Args:
            data (int): new node data.
            next_node (Node): proceeding node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get node data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly list representation."""

    def __init__(self):
        """singly list initalization."""
        self.__head = None

    def sorted_insert(self, value):
        """new node insertion.
        Args:
            value (Node): The Node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ print()  definition of a Linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
