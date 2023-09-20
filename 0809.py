# names = ["Abdulloh", "Abduvali", "Sardor", "Sarvar", "Abubakir"]
# searchWord = input("Kirit: ")

# for item in names:
#     if searchWord.lower() == item[0 : len(searchWord)].lower():               #1 vazifa
#         splited = item.split(" ")
#         print(splited[0])
"===================================================================="

# ls = ["A", "B", "C", "D", "E", "F"]
# number = int(input("Kirit: "))
# alllist = []
# newlist = []

# for item in ls:
#     if(len(newlist) == number):                                    #2 vazifa
#         alllist.append(newlist)
#         newlist = []

#     newlist.append(item)

# alllist.append(newlist)
# print(alllist)
"===================================================================="

# num = int(input())
# counter = 2
# lst = []
# while( num != 1 ):
#     if( num % counter == 0 ):
#         lst.append(counter)
#         num //= counter
#     else:
#         counter += 1

# uniquseList = []
# for item in lst:                                                     #3 vazifa
#     if ( item not in uniquseList ):
#         uniquseList.append(item)

# answer = []
# for item in uniquseList:
#     countItem = lst.count(item)
#     if countItem > 1:
#         answer.append(f"({item} darajasi {countItem})")
#     else:
#         answer.append(f"{item}")

# print(" * ".join(answer))
"===================================================================="

# num = int(input("N: "))
# lst = list(range(1, num + 1)) + list(range(num - 1, 0, -1))
# print(lst)
"===================================================================="

# lst = [ item for item in range( 6 ) if item > 2]
# print(lst)

# lst = [[item for j in range(3)] for item in range(5)]
# print(lst)
"===================================================================="

# lst = [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
# max_count = 0
# count = 0

# for num in lst:
#     if num == 1:
#         count += 1
#         max_count = max(max_count, count)
#     else:
#         count = 0
# print(max_count)
"===================================================================="

# matrix = [[1, 1, 1], 
#           [2, 2, 2], 
#           [3, 3, 3]]
# transposed_matrix = []

# for i in range(len(matrix[0])):
#     row = []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transposed_matrix.append(row)

# print(transposed_matrix)
