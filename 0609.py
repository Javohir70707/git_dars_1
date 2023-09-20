# cardNumber = input("Card number: ")
# checkSumm = 0
# indexItem = 0
# for item in cardNumber:
#     item = int(item)
#     if(indexItem % 2 == 0):
#         item *= 2
#         item = int(item)
#         checkSumm = checkSumm + (item % 10 + item // 10)
#     else:
#         checkSumm += item

#     indexItem += 1

# if(checkSumm % 10 == 0):
#     print("VALID")
# else:
#     print("INVALID")
"==================================================================="
# num = input("Kiriting: ")

# num = int(num)
# num = str(num)[ : : -1]
# num = int(num)
# num = str(num)

# if "0" in num:
#     print("NO")
# else:
#     print("YES")
"==================================================================="
# n = int(input())
# counter = n

# for item in range(1, n + 1):
#     print(" " * (counter - 1), end = "")                                   #uchburchak chiqarish
#     print("* " * item)
#     counter -= 1
"==================================================================="



# ls = list()

# ls = [4, 6, 4, 2, 63, 8, 2]

# print(ls[-1 : : -1])                             #listni teskari qilish
# ls.append(9)                                     #listning orqasiga qoshadi
# ls.extend("vscode")                              #har bitta harfni ajratib ohiriga qoshib chiqadi listlar ham qo'shsa bo'ladi
# t = ls.copy()                                    #boshqa ozgaruvchiga listni copy qilish
# ls.clear()                                       #listni bo'shatish
# ls.insert(0, 80)                                 #ls.insert(index, qiymat) indexga qiymat qoyish
# ls.pop(0)                                        #indexdagi qiymatni ochirish
# ls.remove(63)                                    #qiymatni ochirish
# ind = ls.index(63)                               #qiymatning indexini chiqarish
# ls.sort()                                        #sortlash kichikdan kattagacha
# ls.sort(reverse = True)                          #sortni kattadan kichikga qiladi
# ls.reverse()                                     #listni teskari qilish
# ls = "".join("3022", "9834292")                  #bir biriga yopishtirib chiqarish uchun
# count = ls.count(2)                              #qiymatni listda nechta ekanligini topish
# ls = ls.split(" ")                               #kiritilgan qiymat bo'yicha bo'lib chiqadi

# print(ls)

"==================================================================="

# n = int(input("Son kiriting: "))
# ls = []

# for item in range(n):
#     if item % 2 == 0:
#         ls.append(item)
#     else:
#         ls.insert(0, item)
# print(ls)
"==================================================================="

# ls = [4, 5, 6, 1, 9]
# print(ls[0 : 0])
"==================================================================="




# ls = [
#     "ghlkjdgjkd",
#     [1,4,6,2,6],
#     [4,7,2,8,2],
#     [5,3,7,2,7]
# ]
# print(*ls, sep="\n")
# ls[1].append(80)

# print(ls)
"==================================================================="

# s = "salom qalesan"
# s = s.split(" ")
# print(s)
"==================================================================="

# ls = [1, 1, 2]
# newLs = []
# for item in ls:
#     if item not in newLs:
#         newLs.append(item)
# print(newLs)
"==================================================================="

# filter_list = [1, "a", "b", 0, 15]
# lenght = len(filter_list)

# for i in range(lenght):
#     if type(filter_list[i]) != int:
#         filter_list[i] = None

# while None in filter_list:
#     filter_list.remove(None)

# print(filter_list)
"==================================================================="

# words = ["dog", "cow", "tap", "god", "pat"]
# pairs = []

# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         if words[i] + words[j] == (words[i] + words[j])[ : :-1]:
#             pairs.append([i, j])
#         if words[j] + words[i] == (words[j] + words[i])[ : :-1]:
#             pairs.append([j, i])

# print(pairs)
"==================================================================="

# ls = [1, 3, 8, 1, 8]
# sum_digits = sum(set(ls))
# print(sum_digits)