# lst = [1, 2, 3, 4, 5]
# result = lst[-1]
# for i in range(len(lst) - 2, -1, -1):
#     result = [lst[i], result]
# print(result)
"===================================================================="

# dct = {
#     "name": "Azizbek",
#     "age" : 34,
#     "name": "Sardor",
#     34:"number",
#     5.6:"Aziz",
#     (4, 5) : "Asadbek",
#     True : "Abror",
#     34:"Raqam"
# }

# print(dct["name"])
# print(dct[34])
"===================================================================="

# dct = {
#     "name": "Azizbek",
#     "age" : 34,
#     "name": "Sardor",
#     34:"number",
#     5.6:"Aziz",
#     (4, 5) : "Asadbek",
#     True : "Abror",
#     34:"Raqam"
# }

# print(dct.get("name"))             #keyda tugan ma'lumotni olish
"===================================================================="

# dct = {
#     "name": "Azizbek",
#     "age" : 34,
#     "name": "Sardor",
#     34:"number",
#     5.6:"Aziz",
#     (4, 5) : "Asadbek",
#     True : "Abror",
#     34:"Raqam"
# }

# for key in dct:
    # print(key)                              #hamma keylarni chiqaradi
    # print(dct[key])                           #hamma keylardagi ma'lumotni chiqaradi
    # print(dct.get(key))                      #get() funksiyasini ishlatib ham hamma ma'lumotni olsa bo'ladi
"===================================================================="

# dct = {
#     "name" : "Aziz",
#     "age" : 34
# }
# print("name" in dct)
"===================================================================="

# dct = {
#     "age" : 34
# }
# dct["age"] = 45
# print(dct)
"===================================================================="

# arr = ["A", "B", "A", "A", "A"]
# freq_dict = {}

# for element in arr:
#     if element in freq_dict:
#         freq_dict[element] += 1
#     else:
#         freq_dict[element] = 1

# print(freq_dict)
"===================================================================="

# d = "aagagggg"
# dct = {}

# for i in range(len(d)):
#     if d[i] in dct:
#         dct[d[i]].append(i)
#     else:
#         dct[d[i]] = [i]
# print(dct)
"===================================================================="

# a = "Thomas00LEE0000000043"
# a.split("0")

# b = []
# dct = {}

# for i in a:
#     if i:
#         b.append(i)
"===================================================================="

# dic1={1 : 10, 2 : 20}
# dic2={3 : 30, 4 : 40}
# dic3={5 : 50, 6 : 60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)
"====================================================================="

# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# key_sum = sum(dict1.keys())

# digit_sum = 0
# for digit in str(key_sum):
#     digit_sum += int(digit)

# difference = key_sum - digit_sum

# print(difference)
"====================================================================="

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}

# dict3 = {}

# for key, value in d1.items():
#     dict3[key] = value

# for key, value in d2.items():
#     if key in dict3:
#         dict3[key] += value
#     else:
#         dict3[key] = value

# print(dict3)
"====================================================================="

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}

# for i in d2:
#     if i in d1:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)
"====================================================================="

# ls = [("yellow", 1), ("pink", 2), ("black", 3), ("blue", 4), ("red", 1)]
# ls = dict(ls)
# print(ls)
"====================================================================="

# ls = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
# dict1 = {}

# for key, value in ls:
#     if key not in dict1:
#         dict1[key] = value
#     else:
#         dict1[key] += value

# print(dict1)
"====================================================================="

# ls = [
#         {'name': 'Theodore', 'age': 18}, 
#         {'name': 'Mathew', 'age': 22}, 
#         {'name': 'Roxanne', 'age': 20}, 
#         {'name': 'David', 'age': 18}
#     ]
# max_age = 0
# oldest_name = ""

# for person in ls:
#     if person['age'] > max_age:
#         max_age = person['age']
#         oldest_name = person['name']

# print(oldest_name)
"====================================================================="

# string = "assalomu alaykum qarindoshlar"
# dictionary = {}
# for char in string:
#     if char == " ":
#         continue
#     if char in dictionary:
#         dictionary[char] += 1
#     else:
#         dictionary[char] = 1

# for key in dictionary:
#     print(key + ": " + str(dictionary[key]))
"====================================================================="
# ls = [
#     {"Chemistry": 90},{"Math": 88},{"Physics": 92},{"Chemistry": 87},{"Math": 89},{"Chemistry": 93},{"Physics": 89},{"Math": 90},{"Chemistry": 80},{"Physics": 94},
# ]

# subject_grades = {}

# for item in ls:
#     for subject in item:
#         grade = item[subject]
#         if subject in subject_grades:
#             subject_grades[subject].append(grade)
#         else:
#             subject_grades[subject] = [grade]

# print(subject_grades)
"====================================================================="

