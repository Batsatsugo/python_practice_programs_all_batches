# DECLARE numbers, num, sum_remaining, result

numbers = []

# FOR i in RANGE (10)
# num = ('Enter number {i + 1} ')
# numbers.append(num)
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# sum_remaining = sum(numbers[1:])
# result = numbers[0] - sum_remaining
# PRINT("Result:", result)
