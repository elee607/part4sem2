'''
7_04_Raise.py
Logical exception
'''

def RaiseExample(a):
    if int(a) < 0: 
        raise Exception ("the number is negative")
    else: 
        print ("your age is", a)

def RaiseExample2(a):
    if int(a) < 5: 
        raise Exception ("you're too young for schooling")
    else: 
        print ("Enjoy your schooling")

try:
    a = input("enter your age: ") 
    RaiseExample(a)
    RaiseExample2(a)
except Exception as e:    
    print ("exception: %s" %e)

