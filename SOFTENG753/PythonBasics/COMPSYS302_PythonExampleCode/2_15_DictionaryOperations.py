'''
Dictionary Operations
'''

colours = {'apple':'red', 'banana':'yellow'}
print (colours, type(colours))

print (colours['apple'])    # get value

colours['cherry'] = 'red'   # add
print ("add 'cherry':", colours)

colours['apple'] = 'green'  # update value
print ("update:", colours)

colours.pop('apple')        # delete
print ("pop:", colours)