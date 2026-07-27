'''
6_02_Elif.py
'''

a = input("input any number: ")

if int(a) > 0:
    print ("a is positive")
    print ('OK')
elif int(a) < 0:
    print ("a is negative")
else:
    print ("a is zero")


if int(a) > 0: print ("a is positive")
elif int(a) < 0: print ("a is negative")
else: print ("a is zero")
