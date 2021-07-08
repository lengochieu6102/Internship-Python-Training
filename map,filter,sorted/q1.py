import  math
lst = [10.8932, 12.434, 13.65656]

#Method 1
results = list(map(math.floor,lst))
print(results)

#Method 2
results = list(map(lambda x: math.floor(x), lst))
print(results)

