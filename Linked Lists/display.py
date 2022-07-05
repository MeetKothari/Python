class Node: # class def for node, needed for linked list
    
    def __init__(self, data = None):
        self.data = data    # tweaked, makes more sense to init the next field as null
        self.next = None    # by def, the next field in the last node will be null

class SinglyLinkedList: # class def for linked list
    
    def __init__(self): # init
        self.head = Node()
    
    def length(self):
        
        cur = self.head
        total = 0 # number 0
        
        while cur.next != None:
            total += 1
            cur = cur.next
        return total 
    
    def append(self, data): # append
        new_node = Node(data)   # make new node
        curr = self.head    # set current to leftmost
        while curr.next != None:    # as long as it isn't the last node
            curr = curr.next    # move it up 
        curr.next = new_node    # set new node to the one after it
        
    def insert_at_beginning(self, data): # testing/tweaking needed
        node = Node(data, self.head)
        self.head = node 
    
    def insert_at_end(self, data): # testing/tweaking needed
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def display(self):  # helpful function to display the contents of the linked list
        
        elems = []
        cur_node = self.head
        
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)
        

if __name__ == '__main__':
    
    ll = SinglyLinkedList()
    
    ll.append(1)
    ll.append(2)
    
    # ll.insert_at_beginning(0)

    ll.display()    
    print("The length of the linked list is: ", ll.length())
