# DECLARE number_list, number,

number_list = []

# WHILE TRUE
# TRY
# number = ('Enter a number: ')
# IF number in number_list
# PRINT('duplicate')
# ELSE
# PRINT('unique')
# number_list.append(number)
# EXCEPT ValueError
# PRINT('invalid')
while True:
    try:
        number = int(input("Enter a number: "))
        if number in numberList:
            print("Duplicate")
        else:
            print("Unique")
            numberList.append(number)
    except ValueError:
        print('input is invalid')
