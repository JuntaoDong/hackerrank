#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the deleteNode function below.
def deleteNode(head, position):
    # terminate if linked list is empty
    if not head:
        return
    temp = head
    # if head needs to be removed
    if position == 0:
        head = temp.next
        temp = None
        return head
    # other position needs to be removed
    while position > 1:
        temp = temp.next
        position -= 1
        if temp == None:
            break
    # if position is more than number of nodes
    if temp is None:
        return
    if temp.next is None:
        return
    # store temp.next.next and free up temp.next
    up = temp.next.next
    temp.next = None
    temp.next = up
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
