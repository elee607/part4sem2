'''
3_03_ArgumentPassing.py
'''

a = 100
b = [20]
c = [30]

#def f(a,b):
def f():
    a = 10
    b.append(30)

#f(a,b)
f()
print(a, b)

'''
def g():
    global a
    a = 10
    b.append(40)

g()
print (a, b, c)
'''