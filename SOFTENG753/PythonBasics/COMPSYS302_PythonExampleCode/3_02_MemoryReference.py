'''
3_02_MemoryReference.py
'''

def Times(a, b):
    return a*b

print (Times(10, 20))
print (globals())     # for checking the specifications of function object


myTimes = Times     # allocating "Times" function to different value

print (myTimes(10, 20))
print (globals())
