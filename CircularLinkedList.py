#Python Implementation of Circular Linked List
#Creation, Insertion, Deletion, Traversal

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def check(self, ele):
        if self.head is None:
            return False
        t=self.head
        if t.data == ele:
            return True
        t = self.head.next

    def insert(self, data):
        new_node = Node(data)
        if self.check(data):
            print('Warning: Element already exists!\n')
            return
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = new_node
            # New node will become new tail.
            self.tail = new_node
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head

    # Function to delete a given node from the list
    def deleteNode(self, data):

        # If linked list is empty
        if (self.head == None):
            return

        # If the list contains only a single node
        if ((self.head).data == data and (self.head).next == self.head):
            head = None

        last = self.head
        d = None

        # If head is to be deleted
        if ((self.head).data == data):

            # Find the last node of the list
            while (last.next != self.head):
                last = last.next

            # Point last node to the next of head i.e.
            # the second node of the list
            last.next = (self.head).next
            head = last.next

        # Either the node to be deleted is not found
        # or the end of list is not reached
        while (last.next != self.head and last.next.data != data):
            last = last.next

        # If node to be deleted was found
        if (last.next.data == data):
            d = last.next
            last.next = d.next

        else:
            print("no such keyfound")

        return self.head

    def traverse(self):
        cur = self.head
        if self.head is None:
            print("List is empty\n")
            return
        else:
            while self.head is not None:
                print(cur.data, end=" ")
                cur = cur.next
                if (cur == self.head):
                    break


print("Circular Linked List")
cll = CircularLinkedList()
print("\nInsertion with Traversal Operation")
cll.insert(9)
cll.insert(1)
cll.insert(5)
cll.insert(8)
cll.insert(3)
cll.traverse()
print("\n\nCircular Linked List after deletion of 3")
cll.deleteNode(3)
cll.traverse()