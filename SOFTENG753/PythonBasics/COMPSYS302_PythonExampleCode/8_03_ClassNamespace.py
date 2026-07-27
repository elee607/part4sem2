'''
8_03_ClassNamespace.py
'''

class Person:
    Name = "default"

p1 = Person()
p2 = Person()

print ("Name of p1 instance: " + p1.Name)
print ("Name of p2 instance: " + p2.Name)

p1.Name = "Tom"

print ("Name of p1 instance: " + p1.Name)
print ("Name of p2 instance: " + p2.Name)
