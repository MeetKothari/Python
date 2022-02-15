# class definition

class Stack():

    def __init__ (self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        try:
            self.items.pop()
        except IndexError:
            print("\nNothing left to pop!")

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"\nThe current Stack is: ({self.items})"

# basic initialization
s = Stack()
s.push(2)
s.push(3)

# print it out 
print(s)
print(len(s))
