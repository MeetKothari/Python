# Class Definitions

class Node (object):
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BT (object):
    def __init__ (self, root):
        self.root = Node(root)

    def printBT(self, traversal_type):
        if traversal_type == "preorder":
            return self.preord(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postord(tree.root, "")
        else: 
            print("Invalid Traversal Type!")
            return
    
    def preord(self, start, traversal): # preorder goes from root -> left -> right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preord(start.left, traversal)
            traversal = self.preord(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal): # inorder goes from left -> root -> right
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    def postord(self, start, traversal): # postord goes from left -> right -> root
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal = self.inorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# Sample Tree For Testing

tree = BT(1)                                                #                  1 
tree.root.left = Node(2)                                    #                /   \
tree.root.right = Node(3)                                   #               2     3
tree.root.left.left = Node(4)                               #             /   \
tree.root.left.right = Node(5)                              #            4     5

# Get user input to traverse the tree
val = input ("\nHow would you like to traverse the tree? ")
print (tree.printBT(val))