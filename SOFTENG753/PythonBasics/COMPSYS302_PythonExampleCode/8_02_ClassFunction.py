'''
8_02_ClassFunction.py
'''

class Person:
    Name = "default"
    def PrintName(self):
        print ("My name is " + self.Name)

p1 = Person()
p2 = Person()
'''
# a bound method 
p1.PrintName()
p2.PrintName()
'''

# an unbound method
Person.PrintName(p1)
Person.PrintName(p2)
