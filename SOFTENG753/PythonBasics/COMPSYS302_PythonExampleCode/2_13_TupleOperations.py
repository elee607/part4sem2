'''
Tuple Operations
'''

t = (1, 2, 3, 1)
print (t)
print (type(t))
print (t.count(1)) # counting how many "1" in the tuple


(a, b) = (3, 4)
print (a, b)

a, b = b, a         # swap
print (a, b)

(a, b) = (b, a)     # swap
print (a, b)
