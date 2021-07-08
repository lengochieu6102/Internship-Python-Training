import  itertools as it
list1 = [ ['We', 'are'], 'Novobi']
list2 = [ 'We', ['are', 'Odoo'] ]


result = list(it.chain(list1[0],[list1[1]],[list2[0]],list2[1]))
print(result)