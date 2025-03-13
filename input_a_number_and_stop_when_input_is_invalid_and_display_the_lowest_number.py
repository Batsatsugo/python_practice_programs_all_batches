# DECLARE number_list, number

numberList = []

# WHILE TRUE
# TRY
# number =('Enter a number: ')
# number_list.append(number)
# EXCEPT Value error
# BREAK
while True:
    try:
        number = int(input("Enter a number: "))
        numberList.append(number)
    except ValueError:
        break
        
# PRINT('Lowest number: ', min(number_list))