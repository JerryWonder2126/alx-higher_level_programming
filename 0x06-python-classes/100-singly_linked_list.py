#!/usr/bin/python3
"""This module contains classes that help define a singly linked list"""


class Node:
    """This class defines a node object"""
    def __init__(self, data, next_node=None):
        """
        Args:
        data (int): the data to be added to the node
        next_node (Node): next node to be attached to list
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Retrieves the data of the node"""
            return self.__data

        @data.setter
        def data(self, value):
            """Sets the data of the node"""
            if type(value) != int:
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Retrieves the next node attached to current node"""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """Sets the next_node attached to current node to value"""
            if self.__next_node and type(self.__next_node) != self:
                raise TypeError("next_node must be a Node object")

        def __str__(self):
            return self.data

        def __repr__(self):
            return self.data


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """Initializes this class"""
        self.__head = None

    def insert_head(self, value, next_node=None):
        """
        Inserts a new node at the head position

        Args:
        (int) value: the data to be used to create the node
        (Node) next_node: a node object to be attached to the newly created node
        """
        self.__head = Node(value, next_node)

    def __str__(self):
        """
        The string representation of this class

        Returns: a string
        """
        head = self.__head
        string = ''
        while head != None:
            if head.next_node:
                string += "{}\n".format(head.data)
            else:
                string += "{}".format(head.data)
            head = head.next_node
        return string

    def sorted_insert(self, value):
        if not self.__head:
            self.insert_head(value)
        elif value < self.__head.data:
            self.insert_head(value, self.__head)
        else:
            head = self.__head
            while head.next_node:
                if value >= head.data and value <= head.next_node.data:
                    break
                head = head.next_node

            node = Node(value, head.next_node)
            head.next_node = node
