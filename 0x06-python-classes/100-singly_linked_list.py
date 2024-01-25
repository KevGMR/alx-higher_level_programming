#!/usr/bin/python3
"""
Defines a node of a singly linked list.

Attributes:
- data (int): The data of the node.
- next_node (Node): The next node in the linked list.
"""
class Node:
    """
    Initializes a new node instance.

    Parameters:
    - data (int): The data of the node.
    - next_node (Node, optional): The next node in the linked list(default is None).
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """
    Getter method to retrieve the data of the node.

    Returns:
    - int: The data of the node.
    """
    @property
    def data(self):
        return self.__data

    """
    Setter method to set the data of the node.

    Parameters:
    - value (int): The new data of the node.

    Raises:
    - TypeError: If data is not an integer.
    """
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    """
    Getter method to retrieve the node in the linked list.

    Returns:
    - Node: The next node in the linked list.
    """
    @property
    def next_node(self):
        return self.__next_node

    """
    Setter method to set the next node in the linked list.

    Parameters:
    - value (Node): The new next node in the linked list.

    Raises:
    - TypeError: If next_node is not a node or none.
    """
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

"""
Defines a singly linked list.
"""
class SinglyLinkedList:
    """
    Initializes a new singlylinkedlist instamce with an empty head.
    """
    def __init__(self):
        self.head = None

    """
    Inserts a new Node into the correct sorted position in the list (increasing order).

    Parameters:
    - value (int): The value to be inserted.
    """
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head in None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    """
    Returns a string representation of the linked list.

    Returns:
    - str: A string representation of the linked list.
    """
    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
