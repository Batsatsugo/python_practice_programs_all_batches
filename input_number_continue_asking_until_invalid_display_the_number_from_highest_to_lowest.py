# DECLARE numbers, num

numbers = []

# WHILE TRUE
# TRY
# num = ('Enter a number (or anything else to stop): ')
# numbers.append(num)
# EXCEPT ValueError
# BREAK
while True:
    try:
        num = int(input("Enter a number (or anything else to stop): "))
        numbers.append(num)
    except ValueError:
        break

# SORT NUMBERS FROM HIGHEST TO LOWEST
# numbers.sort(reverse=True)
numbers.sort(reverse=True)  # Sort numbers from highest to lowest

# PRINT('Numbers in descending order:', numbers)