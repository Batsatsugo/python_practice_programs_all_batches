# DECLARE count, sum, num, average

count = 0
sum_numbers = 0

# WHILE TRUE
# TRY
# num = ('Enter a number (or any non-numeric value to stop): ')
# sum += num
# count += 1
# EXCEPT ValueError
# BREAK
while True:
    try:
        num = float(input("Enter a number (or any non-numeric value to stop): "))
        sum_numbers += num
        count += 1
    except ValueError:
        break

# IF count > 0
# average = sum / count
if count > 0:
    average = sum_numbers / count

# PRINT('Average: {average}')
    print(f"Average: {average}")
