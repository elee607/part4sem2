'''
8_06_ClassInheritance.py
'''

class Person:
    Name = "parents"
    PhoneNumber = "021-123-4567"
    
class Student(Person):
    Year = 1

p1 = Student()

print ("Year of p1 instance: {0}".format(p1.Year))
print ("Name of p1 instance: {0}".format(p1.Name))
print ("Phone Number of p1 instance: {0}".format(p1.PhoneNumber))