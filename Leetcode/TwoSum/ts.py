def twosum(arr, target):
    
    table = {} # the mapping will be val : index
    
    for i, n in enumerate(arr): # enumerate() keeps track of the count and an item in a loop.
        
        diff = target - n # create a var to hold desired value
        
        if diff in table: # check to see if desired value is in hash
            
            return [table[diff], i] # return indices
        
        table[n] = i # increment
    
    return # return

sum = twosum([2,7,4,5], 6) # driver to see if it works or not
print(sum)

