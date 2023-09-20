# students = [
#     {"name": "Steve", "notes": [5, 5, 3, -1, 6]},
#     {"name": "John", "notes": [3, 2, 5, 0, -3]}
# ]

# valid_notes = [1, 2, 3, 4, 5]
# notes_distribution = {}

# for student in students:
#     notes = student["notes"]
#     for note in notes:
#         if note in valid_notes:
#             if note in notes_distribution:
#                 notes_distribution[note] += 1
#             else:
#                 notes_distribution[note] = 1

# print(notes_distribution)
"============================================================================="

# def plus(a, b):
#     result = a + b
#     return result

# a = plus(5, 7)
# print(a)
"============================================================================="

# def plus(a, b):
#     print(a + b)

# a = plus(3, 4)
"============================================================================="

# def plus(a = 2, b = 1):
#     print(a + b)

# a = plus()
"============================================================================="

# def plus(a, b ):
#     print(a + b)

# a = plus(b = 5, a = 4)
"============================================================================="

# def plusAll(a = 5, b = 9, *numbers):            #*numbers bir nechta qiymatlarni bitta tuple() ga yig'ib oladi
#     print(numbers)
#     print(a)
#     print(b)

# plusAll(4, 4, 2, 2, 7, 8)
"============================================================================="

# def showNumbers(**args):                          #**args dictionaryga o'tkazadi
#     print(args)

# showNumbers(k = "salom")
"============================================================================="

# lst = [4, 5, 6]
# lst2 = lst
# lst2[0] = 90
# print(lst2)
# print(lst)

# def chnageNumbers(lst):
#     lst[0] = 78

# newLst = [4, 5, 6]
# chnageNumbers(newLst)
# print(newLst)
"============================================================================="








# ls = [3, 6, 1, 7, 2, 7, 34, 9]

# ls = list(map(lambda x: x * 10, ls))
# print(ls)

# ls = list(filter(lambda x: x % 2 != 0, ls))
# print(ls)
"============================================================================="
# data = [{
#     "model": "RDX",
#     "year": 2009
# },{
#     "model": "LS",
#     "year": 2000
# },{
#     "model": "GLK-Class",
#     "year": 2010
# },{
#     "model": "Express 1500",
#     "year": 2005
# },{
#     "model": "LR2",
#     "year": 2008
# },{
#     "model": "XF",
#     "year": 2012
# },{
#     "model": "MR2",
#     "year": 2005
# },{
#     "model": "Malibu",
#     "year": 2007
# },{
#     "model": "M-Class",
#     "year": 2010
# },{
#     "model": "Routan",
#     "year": 2011
# }]

# sorted_data = sorted(data, key=lambda x: x['year'])
# print(sorted_data)
"============================================================================="
# def combine_lists(list1, list2):
#     new_list = []
#     for i in range(max(len(list1), len(list2))):

#         if i < len(list1):
#             new_list.append(list1[i])

#         if i < len(list2):
#             new_list.append(list2[i])                          #2ta listni bittaga qoshish funksiyasi

#     return new_list

# list1 = [1, 2, 3, 4, 5]
# list2 = [11, 22]

# combined_list = combine_lists(list1, list2)
# print(combined_list)
"============================================================================="
#problem 2
# a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# def combine(a,b):
#     result = []
#     for i in a:
#         if i in b:
#             result.append(i)
#     return result

# print(combine(a,b))
"============================================================================="
#problem 3
# ls1 = ["S001", "S002", "S003", "S004"]
# ls2 = ["Adina Park", "Leyton Marsh", "Duncan Boyla", "Saim Richards"]
# ls3 = [85, 98, 89, 92]

# def create_dict(ls1, ls2, ls3):
#     result = []
#     for i in range(len(ls1)):
#         in_dict = {ls2[i]: ls3[i]}
#         out_dict = {ls1[i]: in_dict}
#         result.append(out_dict)
#     return result

# print(create_dict(ls1, ls2, ls3))
"============================================================================="
#problem 4
# dict1 = {1:"ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO"}

# def swap_values(dct):
#     for i in range(1, len(dct), 2):
#         if i+1 in dct:
#             dct[i], dct[i+1] = dct[i+1], dct[i]
#     return dct

# dict1 = swap_values(dict1)
# print(dict1)
"============================================================================="
