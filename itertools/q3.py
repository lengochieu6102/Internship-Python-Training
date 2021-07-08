import  itertools as it

lst = ['Red', 'Green', 'Blue']

temp = list(it.combinations(lst,2))

result = [x+" and "+y for x,y in temp]
print(result)