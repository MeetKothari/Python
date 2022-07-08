# Program to append input strings into an empty stack and return misc. information

def count_stack(s):
    count = len(s)
    return count

stack = []  # default stack

poprequest = input("\nWhat would you like to put into the stack? ") # get req for popping

for c in poprequest:    # as long as there's chracters in input
    
    if poprequest:          
        stack.append(c) # put them into stack
    else:
        print("\nYou need to enter SOMETHING.")
    
    print("\nDone appending element.")  # indicate the successful addition of an element into the stack
    
    
# testing

print("\nLength of stack: ", end = "")
print(count_stack(stack))

print("\nElements: ", end = "")
for i in stack:
    print([i], end = "")

print("\nElements in reverse: ", end = "")
for i in reversed(stack):
    print([i], end = "")

print("\n")
    
