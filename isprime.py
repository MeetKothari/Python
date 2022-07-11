# A program containing different iterations of the 'is_prime' function, a function designed to calculate whether a given integer is a prime number or not.

import timeit

def is_prime_one(n):
    
    if (n == 2 or n == 3): return True          # 2 and 3 are base cases, prime 
    if (n % 2 == 0 or n < 2): return False      # if n = 0 or 1 or n/2 has no remainder, the number is composite      
    
    
    for i in range(3, int(n ** 0.5) + 1, 2):    # only odd n
        if (n % i == 0):
            return False    

    return True

foo = '''   
def is_prime_one(n):
    
    if (n == 2 or n == 3): return True          # 2 and 3 are base cases, prime 
    if (n % 2 == 0 or n < 2): return False      # if n = 0 or 1 or n/2 has no remainder, the number is composite      
    
    
    for i in range(3, int(n ** 0.5) + 1, 2):    # only odd n
        if (n % i == 0):
            return False    

    return True
'''

def is_prime(n):                                # According to u/dawg on stackoverflow, this is one of the faster implementations
    if (n == 2 or n == 3): return True
    if (n < 2 or n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while (f <= r):
        print('\t',f)
        if (n % f == 0): return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

bar = '''
def is_prime(n):                                # According to u/dawg on stackoverflow, this is one of the faster implementations
    if (n == 2 or n == 3): return True
    if (n < 2 or n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while (f <= r):
        print('\t',f)
        if (n % f == 0): return False
        if n % (f + 2) == 0: return False
        f += 6
    return True
'''
    
trial = [1,2,3,4,5,6,7,8,9] # sample testing 

print("\nSample numbers being tested (True if Prime, False if Composite): ")    # test is_prime_one

for i in trial:
    print("{}: ". format(i), end = " "), print(is_prime_one(i))

print("\n")
print("...")
print("\n")

print("\nSample numbers being tested (True if Prime, False if Composite): ")    # test u/dawg's solution

for i in trial:
    print("{}: ". format(i), end = " "), print(is_prime(i))

print("\nFirst, my function's run: ")
print(timeit.timeit(setup = foo, stmt = foo, number = 153467))

print("\nThen, u/dawg's run: ")
print(timeit.timeit(setup = bar, stmt = bar, number = 153467))

print("\nu/dawg wins. His function is faster. :(\n")
