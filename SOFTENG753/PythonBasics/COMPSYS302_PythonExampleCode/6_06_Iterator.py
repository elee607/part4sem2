'''
6_06_Iterator.py
'''

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print(next(iter(mytuple)))
print(next(iter(mytuple)))
print(next(iter(mytuple)))