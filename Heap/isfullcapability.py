# Min-Heap init

class minHeap(self, capacity):
    def __init__(self, capacity):
        self.storage = [0] * capacity # implement the heap using an array
        self.capacity = capacity # set the capacity to the capacity being passed
        self.size = 0 # size being the # of elements currently in the heap (defaults to 0)
        
    # create a series of helper functions to retrieve data     
    
    # the 'index' refers to the inex of the node that you want to find the parent/right/left index of 
       
    def getParentIndex(self, index):
        return (index - 1) // 2 # formula for finding parent indez
    def getRightIndex(self, index):
        return (2 * index + 1)
    def getLeftIndex(self, index):
        return (2 * index + 2)
    
    # another important aspect of heaps is being able to tell whether data exists or not 
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self, index):
        return self.getLeftIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightIndex(index) < self.size
    
    # retireve data from the heap
    
    def getParent(self, index):
        return self.storage[self.getParentIndex(index)]
    def getRight(self, index):
        return self.storage[self.getRightIndex(index)]
    def getLeft(self, index):
        return self.storage[self.getLeftIndex(index)]
    
    # invoker functions
    
    def isFull(self):
        return self.size == self.capacity # invoke before insertion to know whether full or not 
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp # swap data between nides, helpful for heapifying
    
    # An incomplete function that correctly formats the heap and shows it in the terminal
    
    def print_heap(self):
        print("Heap: ")
        print(" " + self.getParentIndex)
        
