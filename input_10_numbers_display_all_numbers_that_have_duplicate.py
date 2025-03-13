# DECLARE numbers, duplicates, num, seen

numbers = []
duplicates = []
# PRINT('Enter 10 numbers: ')
# FOR i IN RANGE(1, 11)
# num = ('Enter a number')
# numbers.append(num)
print("Enter 10 numbers:")
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# find duplicates
seen = set()
for num in numbers:
    if numbers.count(num) > 1 and num not in seen:
        duplicates.append(num)
        seen.add(num)

if duplicates:
    print("Duplicate numbers:", *duplicates)
else:
    print("No duplicates found.")