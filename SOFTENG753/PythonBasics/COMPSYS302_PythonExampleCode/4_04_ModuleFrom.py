'''
4_04_ModuleFrom.py
'''
'''
#import DefineFunction 

from DefineFunction import *
#print (DefineFunction.Times(10, 20))
print (Times(10, 20))
'''


from DefineFunction import Times as myTime
#print (DefineFunction.Times(10, 20))
#print (Times(10, 20))
print (myTime(10, 20))



