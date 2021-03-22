import random, json, math

dicttemp = {}

fp = open("dict_3_standard.json","r")
# str_dict = fp.read()
dict3 = json.load(fp)
# dict3 = decode(str_dict)
# print("dict3 loaded")
fp.close()

count = 1
maxima = max([int(i[1:]) for i in dict3.keys()])
print(maxima)