#node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # insertion operation
    def push(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # traverse method for the linked list
    def print(self):
        current = self.head
        while (current):
            print(current.data, "-->", end=" ")
            current = current.next

def list_concat(L, M):
    temp = M.head
    while temp is not None:
        L.push(temp.data)
        temp = temp.next
    return L

def main():
    L = SinglyLinkedList()
    L.push(1)
    L.push(2)
    print("Linked List(L): ")
    L.print()
    M = SinglyLinkedList()
    M.push(3)
    M.push(4)
    print("\nLinked List(M): ")
    M.print()
    print("\nConcatenated Linked List: ")
    c = list_concat(L, M)
    c.print()

if __name__=="__main__":
    main()


