# DECLARE number_list, number,

number_list = []

# FOR i IN RANGE(1, 11)
# number = ('Enter a number')
# IF number NOT IN number_list
# number_list.append(number)
for i in range(1, 11):
    number = int(input("Enter a number: "))
    if number not in numberList:
        numberList.append(number)

# PRINT(number_list)