# DECLARE even_numbers, num

even_numbers = 0

# FOR i IN RANGE (10)
# num = (Enter number {i + 1} )
# IF num % 2 == 0:
# even_numbers += 1
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_numbers += 1

# PRINT(Total even numbers: , even_numbers)
print("Total even numbers:", even_numbers)