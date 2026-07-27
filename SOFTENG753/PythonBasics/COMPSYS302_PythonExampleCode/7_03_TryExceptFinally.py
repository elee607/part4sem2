'''
7_03_TryExceptFinally.py
'''

try:
    c = 5 / 0
except:
    print ("caught an exception")
else:
    print ("NO exception")
finally:
    print ("always execute")
    
    
print("end")
    