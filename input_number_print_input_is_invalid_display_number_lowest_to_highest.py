# DECLARE number_list, number

numberList = []

# WHILE TRUE
# TRY
# number =('Enter a number: ')
# number_list.append(number)
# EXCEPT ValueError
# BREAK
while True:
    try:
        number = int(input("Enter a number: "))
        numberList.append(number)
    except ValueError:
        break

# PRINT(sorted(number_list))