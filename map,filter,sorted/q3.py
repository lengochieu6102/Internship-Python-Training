lst = [4, -3, 2]

results=sorted(enumerate(lst),key=lambda x:x[0],reverse=True)
results=list(map(lambda x:x[1],results))
print(results)