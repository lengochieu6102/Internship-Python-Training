import  itertools as it
names = ['Thomas Brown', 'Tom Smith','Jane Brown' ,'John Smith']
temp=sorted(names,key=lambda x:x.split()[1])

result=it.groupby(temp,lambda x:x.split()[1])
for k,g in result:
    print(k+" ", list(g))
