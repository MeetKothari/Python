# A bound method is the one which is dependent on the instance of the class as the first argument. 
# It passes the instance as the first argument which is used to access the variables and functions. 
# In Python 3 and newer versions of python, all functions in the class are by default bound methods.

class bound():
    
    def statement(self):
        print("\nThe desired statement is:", self)

Bound = bound()

print(Bound, Bound.statement)

# this is a bound method 