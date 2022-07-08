class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # create stack to hold values before matching 
        
        closetoopen = { ')' : '(', ']' : '[', '}' : '{'} # hash to map the closed brackets to open ones
        
        for c in s: # for character in string
            if c in closetoopen: # if in map
                if stack and stack[-1] == closetoopen[c]: stack.pop() # pop corresponding close bracket
                   else: return False   # if can't, return false
            else:
                stack.append(c) # otherwise, add c to stack
        
        return True if not stack else False # return true if empty, else false (empty stack = valid)
        
       
        
        
