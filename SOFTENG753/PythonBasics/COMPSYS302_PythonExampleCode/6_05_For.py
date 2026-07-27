'''
6_05_For.py
'''

for x in range(1,6):
    print (x, '*', x, '=', x*x)
    
print ("\t")

# list
l = ['apple', 100, 12.34]

for i in l:
    print (i, type(i))

print ("\t")

# dictionary
d = {'apple':1, 'orange':2, 'kiwi':3}

for key, value in d.items():
    print (key + " is $" + str(value) + " per kg")
