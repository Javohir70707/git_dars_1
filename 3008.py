# n = input("Son: ")
# print(n)
# ================================
# a = "salom"

# a = a[0].lower()                        kichik qilish
# print(a)

# a = a.capitalize()                   #katta qilish
# print(a)
# ================================
# word = "Hello"
# print(word[0 : 4])                       0dan 4gacha kesib chiqaradi
# print(word[-2 : -1])                      ohiridan kesib olish


# word = word[3 :]                     shundan boshlab ohirgacha
# word = word[ : -2]                   shundan ohirgacha
# word = word[ : : 3]                   #word[nechinchidan boshlash: nechta element olish: necha qadamdan yurish]
# word = word[ : : -1]                   stringni teskari qilish

# print(word)
# ================================
# word = "saloml"
# word = word.casefold()                 butun stringni kichik harflar qiladi
# word = word.count("l")                 berilgan str ni nechtaligini topadi

# print(word)
# =================================
# a = "salom"

# a = a.capitalize()
# a = a[0].upper() + a[1: -1] + a[-1].upper()
# print(a)
# ================================

# num = 23
# print(f"Mening yoshim {num}da")

# num = 23
# print("Mening yoshim {}".format(num))

# num = input()                                 malumot kiritish
# print(num)

# num = int(input())                            malumot kiritish va intga otkazish
# print(num)
# =================================

# a = 9
# b = 3

# if a % 3 == 0:
#     print("Yes")
# else:
#     print("No")
# ================================

# word = input()
# word = word.lower()
# reverseWord = word[ : : -1]
# if word == reverseWord:
#     print("Polindrom")
# else:
#     print("Not polindrom")
# ================================

# word = input()

# stop = len(word) // 2
# start = stop - 1

# if(len(word) % 2 == 0):
#     print( word[: start] + start[start: stop + 1].upper() + word[stop + 1: ] )
# else:
#     print( word[: stop] + word[stop: stop + 1].upper() + word[stop + 1: ] )
# ================================
str1 = "Assalomu alaykum bootcamp N39"
# print(str1[2:8:])
# ================================



# i = 0
# while i <len(str1):
#     print(i)
#     i += 1
#     break
# else:
#     print(str1)
# =========================
# for i in range(2,6):
#     print(i)

# for i in range(len(str1), -1, -1):
#     str1 = str1.replace("a", "")
    # print(str1[i])
    # print(i)

# str1 = input("str1: ")
# str2 = input("str2: ")

# mix = ""
# i = 0
# j = 0

# while i < len(str1) or j < len(str2):
#     if i < len(str1):
#         mix += str1[i]
#         i += 1
#     if j < len(str2):
#         mix += str2[j]
#         j += 1
# print(mix)
# ==========================================
# str1 = "assalomu alaykum bootcamp foundation n39"
# unique = ""

# for char in str1:
#     if char == " " or char not in unique:
#         unique += char

# print(unique)
# ===========================================
# str1 = "js db3762b 829$#nia*0 215s7sd ns?.,jxhg scx" 
# letters = ""
# for char in str1:
#     if char.isalpha():
#         letters += char

# print(letters)
# ===========================================
# str1 = "js db3d62b 82 9$#nia*0 2y5s786sd ns?.,jxhg scx"
# sum = 0
# number = ""

# for char in str1:
#     if char.isdigit():
#         number += char
#     elif number:
#         sum += int(number)
#         number = ""
# if number:
#     sum += int(number)

# print(sum)
# ============================================

# str1 = "God Ding"
# newStr = ""
# word = ""
# for char in str1:
#     if char == " ":
#         newStr += word[::-1] + " "
#         word = ""
#     else:
#         word += char

# newStr += word[::-1]
# print(newStr)
# ===============================================

