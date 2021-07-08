dict ={'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}
lst1 = ['Key 1', 'Key 5']
lst2= ['Key 2','Key 3']

#check lst1
result1= all(list(map(lambda x:x in dict.keys(),lst1)))
print(result1)

#check lst2
result1= all(list(map(lambda x:x in dict.keys(),lst2)))
print(result1)