import json
Dict = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}

with open('sample.json','w') as outfile:
    json.dump(Dict,outfile,indent=4)

print("Json file: ")
with open('sample.json') as outfile:
    data=json.load(outfile)
    print(data)