'''
3_04_ArgumentSetting.py
'''
c = 50

#def Times(a, b):
def Times(b=30, a=10):
    return a/b

print (Times(10, 20))


print (Times())

print (Times(5))      # a = 5, b = 20

print (Times(b=30))   # a = 10, b = 30

print (Times(b=30, a=20)) 

print (Times(a=20, b=-1)) 
