'''
7_01_TryExcept.py
'''

#c = 5 / 0


try:
    c = 5 / 0
    
#except:
#    print ("caught an exception")

#except ZeroDivisionError:
#    print ("ZeroDivisionError")

except ZeroDivisionError as e:
    print (e)

print("end")