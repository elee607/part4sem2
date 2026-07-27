'''
5_03_AlignmentFormat.py
'''

print ("{0} is {1}".format("apple", "red"))
print ("{0} is {1} or {2}".format("apple", "red", "green"))
print ("{item} is {colour}".format(item="apple", colour="red"))
print ("{item} is {colour}".format(colour="red", item="apple"))

dic = {"item":"apple", "colour":"red"}
print ("{item} is {colour}".format(**dic))

item = "apple"
colour = "green"
print ("{0[item]} is {0[colour]}".format(locals()))
print ("{item} is {colour}".format(**locals()))
