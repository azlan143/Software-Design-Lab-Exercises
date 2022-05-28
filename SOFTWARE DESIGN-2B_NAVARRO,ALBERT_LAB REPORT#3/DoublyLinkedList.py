#Python Implementation of Doubly Linked List
#Creation, Insertion, Deletion, Traversal

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

# ---------insertion operations----------
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        return

        last = self.head
        while last.nref:
            last = last.nref

        last.nref = new_node
        new_node.pref = last
        return

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.nref = self.head

        if self.head is not None:
            self.head.pref = new_node
        self.head = new_node

    def insert_after(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

#----------traversal operations----------
    def forward_traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.nref

    def backward_traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref
#----------deletion operations----------
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked List is now empty")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked List is now empty")
        else:
           n = self.head
           while n.nref is not None:
               n = n.nref
           n.pref.nref =  None

    def delete_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return

        #checks if only one node exist
        if self.head.nref is None:
            #check if value match in the single node in Linked List
            if value==self.head.data:
                self.head = None
            else:
                print(value, "is not present in Linked List")
            return

        #if Linked List contains more than one node
        #check the first node
        if self.head.data == value:
            self.head.pref = None
            return
        #check the middle nodes
        n = self.head
        while n.nref is not None:
            if value == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        #check the last node
        else:
            if n.data == value:
                n.pref.nref = None
            else:
                print(value,"is not present in Linked List")

#Test
print("Doubly Linked List")
dll = DoublyLinkedList()
print("\nInsertion")
dll.insert(1)
dll.insert_begin(0)
dll.insert_after(2)
dll.insert_after(3)
dll.forward_traverse()
print("\n\nDeletion")
dll.delete_value(1)
dll.forward_traverse()
print("\n\nForward Traversal")
dll.forward_traverse()
print("\n\nBackward Traversal")
dll.backward_traverse()







