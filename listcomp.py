# A file playing around with list comprehension and tuple manipulation

mylist = [1,2,3,4,5,6,7,8,9]

mysquaredlist = [i * i for i in mylist] # list comp

print(mylist)
print(mysquaredlist)

mytuple = ("M", "K", "20") # this is a tuple
print(type(mytuple))

name, lname, age = mytuple # unpacking tuple into variables

print(name)
print(lname)
print(age)
