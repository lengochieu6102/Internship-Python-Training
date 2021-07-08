class MyEnum:
    def __init__(self,lst):
        self.lst = list(map(lambda x,y:(y,x),lst,range(len(lst))))
    
    def __iter__(self):
        self.my_iter=iter(self.lst)
        return self

    def __next__(self):
        return next(self.my_iter)

lst=[1,4,9]
enum=MyEnum(lst)
i=iter(enum)
##
print(next(i))
##
for it in enum:
    print(it)

