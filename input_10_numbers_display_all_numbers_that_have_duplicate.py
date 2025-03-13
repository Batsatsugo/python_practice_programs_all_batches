# DECLARE number_list, number, duplicate

number_list = []

# FOR i IN RANGE(1, 11)
# number = ('Enter a number')
# number_list.append(number)
for i in range(1, 11):
    number = (int(input("Enter a number: ")))
    number_list.append(number)

# duplicate = [number for number in number_list if number_list.append(number) == 1]
duplicate = [number for number in number_list if number_list.append(number) == 1]

# PRINT(duplicate)