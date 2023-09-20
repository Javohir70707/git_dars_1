# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_num = find_max(lst[1:])                            #findmax function
#         return lst[0] if lst[0] > max_num else max_num

# lst = [1, 8, 3, 4, 5]
# print(find_max(lst))
"===================================================================="
# def findMax(lst, maxValue = 0, i = 0):
#     if(lst[i] > maxValue):
#         maxValue = lst[i]
#     if(lst[i] == lst[-1]):
#         return maxValue
#     else:                                                       #find Max number in list
#         return findMax(lst, maxValue, i + 1)

# lst = [4, 1, 8, 30, 10]
# a = findMax(lst)
# print(a)
"===================================================================="





# newSet = {7, 3, 1, "salom", True, 9, True, 1, 4.5}                         #set dublicatlarni chiqarmaydi
# print(newSet)

# for item in newSet:
#     print(item)

# print("salom" in newSet)
# print(len(newSet))

# newSet.add(890)                                                #setga qiymat qo'shish
# newSet.add(786)

# print(newSet)
"===================================================================="
# newSet = {7, 3, 1, "salom", True, 9, True, 1, 4.5}

# lst = (50, 6, 5)
# newSet.update(lst)                                             #setga qo'shish
# print(newSet)
"================================================================="
# newSet = {3, 4, 3, 3, 4, 6}
# a = set(newSet)
# b = a.copy                                                      #copy qilish
  
# b.add(7)
# for i in a:
#     print(i)

"==============================================================="

# newSet = {3, 4, 3, 3, 4, 6}
# dct = {"a": 1}

# newSet.clear()                                                     #tozalash
# dct.clear()

# print(newSet)
# print(dct)
"======================================================================="

# newSet = {3, 4, 3, 3, 4, 6}

# newSet.remove(3)                      #qiymatni o'chirish
# newSet.discard(3)

# print(newSet)


