#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get/set the data of the Node."""
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be integer")
            slef.__data = value

        @property
        def next_node(self):
            """Get/set the next_node of the Node."""
            return(self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the SignlyLinkedList.
        The Node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
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
