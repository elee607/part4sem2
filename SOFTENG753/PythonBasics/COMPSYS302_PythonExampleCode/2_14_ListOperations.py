'''
List Operations
'''

colours = ['red', 'green', 'gold']
print (colours, type(colours))

colours.append('blue')
print ("append:", colours)

colours.insert(1, 'black')
print ("insert:", colours)

colours.extend(['white', 'gray'])
print ("extend:", colours)

colours += ['red']
print ("+=[]:", colours) # extend / append

colours += 'red'
print ("+='':", colours)

print ("index0 'red':", colours.index('red'))
#==> ['red'0, ...... 'red'7]

print ("index1 'red':", colours.index('red', 1))

print ("count 'red':", colours.count('red'))

colours.pop()
print ("pop:", colours)

colours.pop(1)
print ("pop(1):", colours)

colours.remove('red')
print ("remove 'red':", colours)

colours.sort()
print ("sort:", colours)

colours.reverse()
print ("reverse:", colours)
#'''