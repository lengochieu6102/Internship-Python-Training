Dict = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}

result=sum(list(map(len,Dict.values())))
print(result)