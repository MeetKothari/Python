# Min-Heap init

class minHeap(self, capacity):
    def __init__(self, capacity):
        self.storage = [0] * capacity # implement the heap using an array
        self.capacity = capacity # set the capacity to the capacity being passed
        self.size = 0 # size being the # of elements currently in the heap (defaults to 0)
