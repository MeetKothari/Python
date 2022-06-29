class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def print_right(self):
        print("The index is: ", self.next)
        print("The data field of the node is: ", self.data)
        
a = node(2, 1) # initialize with random variables
a.print_right() # trivial function to double-check whether the initialization worked or not
