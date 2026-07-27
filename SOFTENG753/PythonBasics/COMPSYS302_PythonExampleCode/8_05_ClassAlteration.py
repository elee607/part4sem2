'''
8_05_ClassAlteration.py
'''

class Person:
    name = "class"
Person.year = 1

p1 = Person()
p2 = Person()
print ("Year of p1 instance: {0}".format(p1.year))
print ("Year of p2 instance: {0}".format(p2.year))
print("\t")

p1.year = 3
print ("Year of p1 instance: {0}".format(p1.year))
print ("Year of p2 instance: {0}".format(p2.year))
print("\t")

p3 = Person()
print ("Year of p3 instance: {0}".format(p3.year))
print("\t")

p2.__class__.year = 2
print ("Year of p1 instance: {0}".format(p1.year))
print ("Year of p2 instance: {0}".format(p2.year))
print("\t")

p4 = Person()
print ("Year of p4 instance: {0}".format(p4.year))
print("\t")
