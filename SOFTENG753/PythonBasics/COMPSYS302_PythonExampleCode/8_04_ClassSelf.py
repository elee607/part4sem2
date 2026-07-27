'''
8_04_ClassSelf.py
'''

name = "global" 

class Person:
    name = "default"
    def PrintName(self):
        print ("self.name is " + self.name) # local 
        print ("name is " + name)           # global

p1 = Person()
p1.PrintName()      # a bound method