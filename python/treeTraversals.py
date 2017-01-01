
# take input some numbers to construct a tree. A BST

print('How many elements in the tree:')
num = int(input())





class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def pInsert(self, value, t):
        if t.val < value:
            if t.right == None:
                t.right = Node(value)
            else:
                self.pInsert(value,t.right)
        else:
            if t.left == None:
                t.left = Node(value)
            else:
                self.pInsert(value, t.left)
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.pInsert(value,self.root)
    def pInorderTraversal(self,t):
        if t != None:
            self.pInorderTraversal(t.left)
            print(t.val, end = ' ')
            self.pInorderTraversal(t.right)
    def inorderTraversal(self):
        if self.root != None:
            self.pInorderTraversal(self.root.left)
            print(self.root.val, end=" ")
            self.pInorderTraversal(self.root.right)

#create a BST with the input numbers
bst = BST()
for i in range(num):
    bst.insert(int(input()))
print("Inorder traversal")
bst.inorderTraversal()
#print a new line
print()

