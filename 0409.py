# word = "hhhhhheeeelllllooooo"
# word = word.lower()
# letterCount = ""
# i = 0

# while i < len(word):
#     if ( word[i] not in letterCount):
#         letterCount += word[i]        
#         print("{} - {}".format(word[i], word.count(word[i])))
#     i += 1

# print(letterCount)

"==============================================================================="

# word = "hhhhhheeeelllllllllllllllooooo"
# newWord = ""
# j = 0
# while j < len(word):
#     if word[j] not in newWord:
#         newWord += word[j]
#     j += 1
#     print(newWord)

# maxRepitedItem = newWord[0]
# maxRepitedCount = word.count(maxRepitedItem)

# i = 0

# while i < len(newWord):

#     countItem = word.count(newWord[i])

#     if maxRepitedCount < countItem:
#         maxRepitedCount = countItem
#         maxRepitedItem = newWord[i]

#     i += 1

# print(maxRepitedItem)

"==============================================================================="

# word = "W? sta$t les$*n"
# letters = "erso"
# j = 0

# i = 0
# while i < len(word):
#     if (not word[i].isalnum() and not word[i].isspace() ):
#         word = word.replace(word[i], letters[j], 1)
#         j += 1
#     i += 1
# print(word)

"==============================================================================="

# word = "hello we start lesson"

# for item in "salom":
#     print(item)

"==============================================================================="

# limit = range(1, 5)            # 1 dan 5 gacha sonlar bor

# for item in limit:
#     print(item)

"==============================================================================="

# stop = int(input("Kirit: "))

# limit = range(0, stop, 1)

# for item in limit:
#     print(item)

"==============================================================================="

# valid = input("Number: ")
# flag = 1
# for item in valid:
#     if( not item.isspace() and item.isdigit() and (len(valid) == 4 or len(valid) == 6) ):
#         flag = 0
#     else:
#         flag = 1
#         break

# if flag == 0:
#     print(True)
# else:
#     print(False)

"==============================================================================="

# word = input("Kiriting: ")
# newWord = ""

# for item in word:
#     if item == "z":
#         newWord += "a"
#     else:
#         newWord += chr( ord(item) + 1 )

# print(newWord)

"==============================================================================="

# num = input("Kiriting: ")
# flag = True
# for item in range(10):
#     if str(item) not in num:
#         flag = False
#         break

# print(flag)

"==============================================================================="

# num = int(input("Kirit: "))
# counter = 0
# while num >= 2:
#     counter += 1
#     num = num ** 0.5

# print(counter)

"==============================================================================="

# sentence = input("Введите предложение: ")

# duplicates = sum(sentence.lower().count(char) > 1 for char in sentence.lower() if char.isalpha())

# print(f"{duplicates}")

"==============================================================================="





# pass                 for da shunchaki otkazib probellarni orniga turadi, agar shart yozilmasa

# num = input("Son kiriting: ")
# sumDigits = 0

# for i in range(len(num)):
#     sumDigits += int(num[i])

# print(sumDigits)
"==============================================================================="

# ls = list()

# ls = ["qalesan", 4, 6, 4.6, 2.7, "salom", True, False]

# print(ls[0])                             #faqat birinchisi string bolsa ishlaydi
"==============================================================================="

# ls = list()

# ls = [4, 6, 4.6, 2.7, ["fhdjfk", "skkf"], True, False]
# print(ls[4][1][0])
"==============================================================================="

# ls = list()

# ls = [4, 6, 4, 2, 63, 8, 2]

# print(ls[-1 : : -1])                             #listni teskari qilish
# ls.append(9)                                     #listning orqasiga qoshadi
# ls.extend("vscode")                              #har bitta harfni ajratib ohiriga qoshib chiqadi listlar ham qo'shsa bo'ladi
# t = ls.copy()                                    #boshqa ozgaruvchiga listni copy qilish
# ls.append(90)                                    #ohiriga qoshadi
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
# print(ls)
"==============================================================================="

# ls = list()
# ls = [i for i in range(1, 6)]
# for i in range(1, 6):
#     ls.append(i)
# print(ls)
"==============================================================================="

# numbers = [11, 313, 50]
# newNumber = ""

# for num in numbers:
#     newNumber += str(num)

# print(newNumber)
"==============================================================================="

# ls = [1, 2, 3, 4]
# string = "emp"
# result = []

# for i in ls:
#     result.append(string + str(i))

# print(result)
"==============================================================================="

# ls = [1, 0, 2, 0, 3, 4, 0, 0,5]
# result = []

# for i in ls:
#     if i != 0:
#         result.append(i)

# for i in range(ls.count(0)):
#     result.append(0)

# print(result)
"==============================================================================="

# ls = ["apple", "coin", "pink", "black", "black", "pink", "pink"]
# newLs = []

# for item in ls:
#     if item not in newLs:
#         newLs.append(item)

# print(newLs)
"==============================================================================="

# ls = ["apple", "elem", "mango", "onion"]

# result = "Yes"

# for i in range(len(ls) - 1):
#     current_word = ls[i]
#     next_word = ls[i + 1]

#     if current_word[-1] != next_word[0]:
#         result = "No"
#         break

# print(result)
"==============================================================================="

# ls = [[7, 4, 5, 1], [2, 3, 6]]
# combined_list = ls[0] + ls[1]
# combined_list.sort()
# for i in range(len(combined_list)-1):
#     if combined_list[i+1] - combined_list[i] != 1:
#         print(False)
#         break
# else:
#     print(True) 
"================================================================================"


# ls = ["cow", "cow", "pig", "cow", "pen", "pen"]
# countWord = {}
# for word in ls:
#     if word in countWord:
#         countWord[word] += 1
#     else:
#         countWord[word] = 1

# result_list = []
# for word, countWord in countWord.items():
#     if countWord >= 2:
#         result_list.append(word + "s")
#     else:
#         result_list.append(word)

# print(result_list)
"================================================================================"

# ls = [4, 1, 4]
# minNum = ls[0]
# total = 0

# for i in range(1, len(ls)):
#     if ls[i] < minNum:
#         minNum = ls[i]

# for i in range(len(ls)):
#     if ls[i] != minNum:
#         percent = ls[i] * 0.25
#         ls[i] -= percent
#         total += percent

# minNum += total
# print(ls)
"================================================================================"

