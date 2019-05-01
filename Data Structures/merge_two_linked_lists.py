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

# Complete the mergeLists function below.
def mergeLists(head1, head2):
    # if head1 is empty, return head2
    if not head1:
        return head2
    # if head2 is empty, return head1
    if not head2:
        return head1
    # select the head for the merged list
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    # start merge
    temp = head
    while True:
        if head1 == None and head2 != None:
            temp.next = head2
            break
        elif head2 == None and head1 != None:
            temp.next = head1
            break
        elif head1 and (head1.data <= head2.data):
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        elif head2 and (head2.data < head1.data):
            temp.next = head2
            temp = temp.next
            head2 = head2.next
        else:
            break
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
