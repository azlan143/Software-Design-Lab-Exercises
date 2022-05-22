#Python Implementation of Singly Linked List
#Creation, Insertion, Deletion, Traversal

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    #insertion operation
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    #deletion operation
    def delete(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    # traverse method for the linked list
    def traverse(self):
        current = self.head
        while (current):
            print(current.data, end = " ")
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

#Test
mylist = SinglyLinkedList()
print("Single Linked List: ")
mylist.insert(1)
mylist.insert(2)
mylist.insert(3)
#Created Single Linked List using insertion and deletion operation
print("\nInsertion: ")
mylist.traverse()
mylist.delete(2)
print ("\n\nLinked List after Deletion at position 2:")
mylist.traverse()
print ("\n\nLinked List before backward traversal:")
mylist.traverse()
print ("\n\nLinked List after backward traversal:")
mylist.reverse()
mylist.traverse()