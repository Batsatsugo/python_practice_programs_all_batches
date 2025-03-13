# SET count to 0
count = 0

# FOR i FROM 1 TO 10 DO
# PRINT Enter a number , i, :
# INPUT num
# IF num MOD 2 NOT EQUAL TO 0 THEN
# COUNT = COUNT + 1
for i in range(10):
    num = int(input(f'Enter a number {i + 1}: '))
    if num % 2 != 0:
        count += 1
# ENDIF

# PRINT number of odd numbers: , count
print(f'Number of Odd Numbers: {count}')