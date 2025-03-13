# DECLARE highest, num

highest = None
# highest = None
# WHILE TRUE
# TRY
# num = ('Enter a number (or any non-numeric value to stop): ')
# IF highest IS None or num > highest
# highest = num
# BREAK
while True:
    try:
        num = int(input("Enter a number (or any non-numeric value to stop): "))
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

# IF highest IS NOT None
# PRINT('The highest number entered was: ', highest)
if highest is not None:
    print("The highest number entered was:", highest)
