# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")
      
# Subtraction
num3 = float(input("Enter the first number for subtraction: "))
num4 = float(input("Enter the second number for subtraction: "))
diff_result = num3 - num4
print(f"difference: {num3} - {num4} = {diff_result}")

# Multiplication
num5 = float(input("Enter the first number for multiplication: "))  
num6 = float(input("Enter the second number for multiplication: "))
product_result = num5 * num6
print(f"product: {num5} * {num6} = {product_result}")

# Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
 print("Error: Division by zero is not allowed.")
else:
 div_result = num3 / num4
 print(f"Division: {num3} / {num4} = {div_result}")