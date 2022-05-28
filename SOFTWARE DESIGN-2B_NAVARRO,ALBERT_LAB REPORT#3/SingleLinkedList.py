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
    def delete(self, x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if x==self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Node is not present")
        else:
            n.next=n.next.next

    # traverse method for the linked list
    def traverse(self):
        current = self.head
        while (current):
            print(current.data, "-->", end = " ")
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
mylist.insert(4)
#Created Single Linked List using insertion and deletion operation
print("\nInsertion: ")
mylist.traverse()
mylist.delete(4)
print ("\n\nLinked List after Deletion of node 4:")
mylist.traverse()
print ("\n\nLinked List before backward traversal:")
mylist.traverse()
print ("\n\nLinked List after backward traversal:")
mylist.reverse()
mylist.traverse()