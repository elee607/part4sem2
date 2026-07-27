'''
3_05_LambdaExpression.py
'''
'''
def Times(a, b):
    return a*b
'''
g = lambda a, b : a*b

print (g(10, 20))

print (lambda a=5, b=10 : a*b)

print (lambda a, b : a*b(5,10))
