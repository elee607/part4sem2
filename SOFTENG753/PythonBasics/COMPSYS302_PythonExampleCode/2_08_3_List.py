'''
#Tuples
aa = (12345,)
print ("aa =", aa)
'''
#Lists
a = [12345,]
print ("a =", a)

b = list ['hello']
#b = list ('hello')
#b = ['h', 'e', 'l', 'l', 'o']
print ("b =", b)

c = [1, 2, 'hello']
print ("c =", c)
print ("c[0] =", c[0])
print ("c[1:40] =", c[1:40])
#==> start from the index 1 and till the index 2
print ("c[-1] =", c[-1])

c[0] = "melon"
print ("c =", c)