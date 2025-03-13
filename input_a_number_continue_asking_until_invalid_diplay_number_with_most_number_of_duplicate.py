# DECLARE numbers, num, most_repeated
# WHILE TRUE
# TRY
# num =('Enter a number: ')
# IF num IN numbers
# numbers[num] += 1
# ELSE
# numbers[num] = 1
# EXCEPT ValueError
# BREAK
# IF numbers
# most_repeated = max(numbers, key=numbers.get)
# PRINT(f"The number with the most duplicate is: {most_repeated}")