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
    
    def get_data_from(self, index):
        
        
        if index >= self.length():
            print("Index is of out of range.")
            return 
        
        curr_index = 0
        curr_node = self.head
        
        while True:
            
            curr_node = curr_node.next
            
            if curr_index == index: return curr_node.data
            
            curr_index += 1
            
             
    def erase_data_from(self, index):
        
        if index >= self.length():
            print("Index is out of range.")   
            return None
        
        curr_index = 0
        curr_node = self.head
        
        while True:
            
            last_node = curr_node
            curr_node = curr_node.next
            
            if curr_index == index:
                last_node.next = curr_node.next
                return 
        
            curr_index +=1  
        
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
    ll.append(3)
    ll.append(4)
    
    # ll.insert_at_beginning(0)

    ll.display()    
    print("The length of the linked list is: ", ll.length())
    print("The element at the second index is: ", ll.get_data_from(2))
    
    print("After erasing the element at the second index, the linked list is: ")
    ll.erase_data_from(2)
    ll.display()
   
