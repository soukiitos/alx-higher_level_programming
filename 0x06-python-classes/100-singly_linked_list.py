#!/usr/bin/python3
'''Define a node of a singly linked list'''


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


'''Define a singly linked list'''


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        a = Node(value)
        b = self.__head
        add_start = False
        if self.__head:
            if value < self.__head.data:
                add_start = True
            while b.next_node and value > b.next_node.data and not add_start:
                b = b.next_node
            if not add_start:
                a.next_node = b.next_node
                b.next_node = a
            else:
                a.next_node = b
                self.__head = a
            a.data = value
        else:
            self.__head = a
            a.next_node = None
    def __str__(self):
        s = ""
        c = self.__head
        while c:
            s += str(c.data) + '\n'
            c = c.next_node
        return s[: -1]
