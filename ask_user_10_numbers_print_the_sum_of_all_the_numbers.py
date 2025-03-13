# total = 0
total = 0

# FOR i FROM 1 TO 10 DO
# DISPLAY "Enter number ", i, ": "
# INPUT num
# total = total + num
for i in range (10):
    num = int(input(f'Enter number {i + 1}: '))
    total += num
# END FOR

# PRINT "The sum of 10 numbers is: ", total
print('The sum of 10 numbers is: ', total)