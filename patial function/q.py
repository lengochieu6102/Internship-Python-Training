from functools import *
def multiply(x, y):
    return x * y
doubleNum=partial(multiply,2)
tripleNum=partial(multiply,3)

print(doubleNum(4))
print(tripleNum(5))