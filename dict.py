dict = {
    "a" : [1,2],
    "b" : 2,
    "c": 3,
}

# print(dict)
# #update--------------

# dict['a'] = 'kabuto'
# print(dict)
# #acessing the value -----------------
# print(dict.keys())
# print(dict.values())
# print(dict['c'])

# print(dict.get('a'))

# for i,j in dict.items():
#     print(i,j)

# #adding new key value-----------------
# dict['dabu']= 'bato'

# print(dict)
# #remove ----------------
# dict.pop('dabu')

# del dict['a']
# print(dict)
# #acess with index number
# for i, (k,v) in enumerate(dict.items(),1):
#     print(i,k,v)

# from collections import defaultdict


# d = defaultdict(int)
# d1 = {}
# d['x'] +=1
# d['x'] += 1
# print(d)


# s = "hello"
# count = defaultdict(int)
# for i in s:
#     count[i] += 1
# print(count)

# words = ['eat','tea','tan']
# groups = defaultdict(list)
# for word in words:
#     key = "".join(sorted(word))
#     groups[key].append(word)
# print(groups) 

# dd = defaultdict(int)
# string = "mississippi"
# for i in string:
#     dd[i] += 1
# print(dd)

# group = defaultdict(int)
# nums = [1,3,4,2,5,6,7,8,9,10]
# for i in nums:
#     if i%2 == 0:
#         groups['even'].append(i)
#     else:
#         groups['odd'].append(i)
# print(groups)


dict2 = {"av":"car","dum":"dumbo"}
print(dict2.keys())
    