'''
Set Operations
'''

a = {1, 2, 3}
b = {3, 4, 5}
#b = {3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3}

print (a, b)
print (a.union(b), a|b)           # union
print (a.intersection(b), a&b)    # intersection
print (a-b)                       # difference set 
