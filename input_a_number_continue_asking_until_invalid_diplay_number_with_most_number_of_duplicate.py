# DECLARE numbers, num, most_repeated

numbers = {}

# WHILE TRUE
# TRY
# num =('Enter a number: ')
# IF num IN numbers
# numbers[num] += 1
# ELSE
# numbers[num] = 1
# EXCEPT ValueError
# BREAK
while True:
    try:
        num = int(input("Enter a number: "))
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1
    except ValueError:
        break


# IF numbers
# most_repeated = max(numbers, key=numbers.get)
# PRINT(f"The number with the most duplicate is: {most_repeated}")