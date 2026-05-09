limit = int(input("Enter the limit: "))

# Initialize the sum
total = 0

# Use a for loop to calculate the sum
for i in range(1, limit + 1):
    total += i

# Print the sum
print("The sum of natural numbers up to", limit, "is:", total)