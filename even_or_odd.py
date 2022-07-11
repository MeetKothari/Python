# A program with functionality to identify odd numbers and print out the first 'n' of them.

def even_or_odd(i):
    if (i % 2) == 0:
        print("Even.")
    else: print("Odd.")
    
    
# testing

count = 0   # var 
trial = [1,2,3,4,5,6,7,8,9] # sample testing 

print("\nSample numbers being tested: ")

for i in trial:
    print("{}: ". format(i), end = " "), even_or_odd(i)
    
trial2 = input("\nWhat number should the program test until? ")     # takes user input and displays even/odd within given range
print("\nThe program will test from 0 to {}.". format(trial2))      # display the range to the user

while count <= int(trial2):                                         # while the count var is less than or equal to the given upper limit:
    print("{}: ". format(count), end = " "), even_or_odd(count)          # calc 
    count += 1                                                      # increment
    
