# DECLARE number_list, number, non_duplicated

number_list = []
# FOR i IN RANGE(1, 11)
# number = ('Enter a number')
# number_list.append(number)
for i in range(1, 11):
    number = int(input("Enter a number: "))
    number_list.append(number)

# non_duplicated = [number for number in number_list if number_list.count(number) == 1
non_duplicated = [number for number in number_list if number_list.count(number) == 1]

# PRINT(non_duplicated)
print(non_duplicated)