import json

with open('dict_3_standard.json','r') as f:
    dict3 = json.load(f)

maxima = max([int(i[1:]) for i in dict3.keys()])

keys_ = []
values_ = []
for i in range(1, maxima+1):
    keys_.append(dict3[f'k{i}'])
    values_.append(dict3[f'v{i}'])

new_dict3 = {
    'keys_': keys_,
    'values_': values_
}

with open('dict_3_standard_2.json','w') as f:
    json.dump(new_dict3, f,sort_keys=True)