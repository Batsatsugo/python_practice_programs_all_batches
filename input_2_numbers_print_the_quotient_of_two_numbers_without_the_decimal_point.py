# DECLARE first_number, second_number, quotient

# INPUT first_number
first_number = int(input('Enter first number: '))

# INPUT second_number
second_number = int(input('Enter first number: '))

# IF second_number not equal to 0
# quotient = first_number // second_number
# PRINT ("Quotient: ", quotient)
if second_number != 0:
    quotient = first_number // second_number
    print("Quotient:", quotient)

# ELSE
# PRINT ("Error: Division by zero is not allowed")
else:
    print("Error: Division by zero is not allowed.")