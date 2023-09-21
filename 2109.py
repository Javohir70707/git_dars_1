# with open("Karta.txt", 'r', encoding='utf-8') as file:
#     count = 0
#     for line in file:
#         if "mastercard" in line:
#             count += 1

# print(count)



# 5007669544563319,mastercard,Euro,EUR,Major Chemicals,France
# 5108756348035400,mastercard,Euro,EUR,Farming/Seeds/Milling,France

def count_countries_with_mastercard(filename):
    countries = set()
    
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if 'mastercard' in data[1].lower():
                countries.add(data[5])
    return len(countries)

filename = "Karta.txt"
count = count_countries_with_mastercard(filename)
print(count)
