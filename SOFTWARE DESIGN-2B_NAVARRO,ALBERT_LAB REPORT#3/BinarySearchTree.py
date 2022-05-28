#BINARY SEARCH TREE
class BST:
    def __init__(self, key):
        self.key  = key
        self.lchild = None
        self.rchild =None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        #ignore duplicate value
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                #create a new node
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                #create a new node
                self.rchild = BST(data)

    def traverse_preorder(self):
        #visit the root node
        print(self.key, end = " ")
        #check the left subtree
        if self.lchild:
            self.lchild.traverse_preorder()
        #check the right subtree
        if self.rchild:
            self.rchild.traverse_preorder()

    def traverse_postorder(self):
        #visit the lchild
        if self.lchild:
            self.lchild.traverse_postorder()
        #visit the rchild
        if self.rchild:
            self.rchild.traverse_postorder()
        #visit the root node
        print(self.key, end = " ")

    def traverse_inorder(self):
        #visit the lchild
        if self.lchild:
            self.lchild.traverse_inorder()
        print(self.key, end = " ")
        #visit the rchild
        if self.rchild:
            self.rchild.traverse_inorder()

#A function to count no. of nodes.
def counter(root, count):
    if root:
        #First recur the left child
        if root.lchild:
            count = counter(root.lchild, count)
        count += 1
        #Recur the right child at last
        if root.rchild:
            count = counter(root.rchild, count)
        return count

root = BST(100)
mylist = [9, 1, 5, 8, 3, 4, 2]
for i in mylist:
    root.insert(i)
print("Root Node:", 100)
print("Pre-order traversal of binary tree:")
root.traverse_preorder()
print("\nPost-order traversal of binary tree:")
root.traverse_postorder()
print("\nIn-order traversal of binary tree:")
root.traverse_inorder()
count = 0
count = counter(root, count)
print("\nTotal number of nodes in binary tree:", count)

