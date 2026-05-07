# Input the interval from the user
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

# Iterate through the numbers in the interval
for num in range(lower, upper + 1):

    # Find the number of digits in 'num'
    order = len(str(num))

    temp_num = num
    total = 0

    # Calculate sum of digits raised to the power of number of digits
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** order
        temp_num //= 10

    # Check if 'num' is an Armstrong number
    if num == total:
        print(num)