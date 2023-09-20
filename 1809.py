# print("yes 1")
# print("yes 2")

# try:                                           #kod yoziladi
#     int("Hello")
# except:                                        # agar hato bo'lsa ishlaydi
#     print("Hato")
# print("yes 3")

"======================================================================================="


# print(dir(__builtins__))                        #hamma hatolarni chiqarib beradi

"======================================================================================="


# file = open("data.txt", "w")
# file.write("Hello world")                         #filega yozuv qo'shish
# file.close()


# file = open("data.txt", "r")
# a = file.read(3)                             #shuncha elemntini olish
# a = file.readline(500)                         #bitta qatorni olish
# a = file.readlines(26)
# print(a)
"======================================================================================="

# with open("data.txt", "r") as file:
#     a = file.read()
#     print(a)
"======================================================================================="

# import json

# data = [None, True, 3.4, {8: 5}]

# with open("users.json", "w") as file:
#     converted = json.dumps(data)
#     file.write(converted)

# with open("users.json", "r") as file:
#     a = file.read()
#     converted = json.loads(a)
#     print(converted)
"======================================================================================="
# from uuid import uuid4
# from json import dumps, loads

# def getUsers():
#     with open("users.json", "r") as file:
#         userData = file.read()
#         convertedData = []
#         if userData:
#             convertedData = loads(userData)

#         return convertedData
    



# def createUser(name, age, phone):

#     allData = getUsers()
#     userData = {
#         "name": name,
#         "id": uuid4(),
#         "age": age,
#         "phoneNumber": phone
#     }
    
#     allData.append(userData)
#     with open("users.json", "w") as file:
#         file.write(dumps(allData, indent=4))


# createUser("Aziz", 45, "998903298765")
"======================================================================================="

# from json import dumps, loads

# with open("names.json", "r") as file:
#     data = file.read()
#     if data:
#         data = loads(data)
#     else:
#         data = {}

# name = input("Fruit name: ")

# if data.get(name) != None:
#     data[name] += 1
# else:
#     data[name] = 1


# with open("names.json", "w") as file:
#     file.write(dumps(data, indent=4))