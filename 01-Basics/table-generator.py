# Generates a multiplication table for a user-specified number and range.

target = int(input("Enter the number to multiply: "))
limit = int(input("Enter the maximum range: "))

for i in range(1, limit + 1):
    print(f"{target} * {i} = {i * target}")
