class Node(object): # class def for node, needed for linked list
    
    def __init__(self, data):
        self.data = data    # tweaked, makes more sense to init the next field as null
        self.next = None    # by def, the next field in the last node will be null

class SinglyLinkedList(object): # class def for linked list
    
    def __init__(self): # init
        self.head = Node()
    
    def append(self, data): # append
        new_node = Node(data)   # make new node
        curr = self.head    # set current to leftmost
        while curr.next != None:    # as long as it isn't the last node
            curr = curr.next    # move it up 
        curr.next = new_node    # set new node to the one after it
    
