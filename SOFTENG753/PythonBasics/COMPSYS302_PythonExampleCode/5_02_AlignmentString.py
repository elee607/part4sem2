'''
5_02_AlignmentString.py
'''

for x in range(1,6):
    print (x, '*', x, '=', x*x)

print ('\n')  
  
for x in range(1,6):
    print (x, '*', x, '=', str(x*x).rjust(5))

print ('\n')  
    
for x in range(1,6):
    print (x, '*', x, '=', str(x*x).ljust(3))

print ('\n')  

for x in range(1,6):
    print (x, '*', x, '=', str(x*x).center(3))
    
print ('\n')  

for x in range(1,6):
    print (x, '*', x, '=', str(x*x).zfill(3))
