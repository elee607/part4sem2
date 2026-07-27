'''
5_05_FileIO.py
'''

f = open('test.txt', 'a')
f.write("Hello. This message is from the file")
f.close()

f = open('test.txt', 'r')
print (f.read())
f.close()

#print (f.closed)