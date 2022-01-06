def recursivefib(n):
    if n <= 2:
        return 1
    else:
        return (recursivefib(n-1) + recursivefib(n-2))

# print (recursivefib(2))   
# print (recursivefib(3))
# print (recursivefib(4))

ask = int(input("\nPlease enter a nonzero integer to find its corresponding Fib. number: "))

if ask <= 0:
    print("\nInvalid input!\n")
else:
    print("\nFibonacci counterpart of your number is: \n")
    print(recursivefib(ask))
    print("\n")

