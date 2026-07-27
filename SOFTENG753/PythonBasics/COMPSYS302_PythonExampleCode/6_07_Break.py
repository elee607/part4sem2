'''
6_07_Break.py
'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in l:
    if i > 5:
        print ("break - terminate loop!!")
        break
    print (i)
    
print ("ourside of the for loop - break")

print("  ")

for i in l:
    if i > 5:#i % 2 == 0:
        print ("continue - keep going!!")
        continue
    print (i)
        
print ("ourside of the for loop - continue")
    