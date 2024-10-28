# Input the number and range for the multiplication table
number = int(input("Enter the number for the multiplication table: "))
range_limit = int(input("Enter the range for the table: "))

print(f"\nMultiplication Table for {number}:\n")

# Loop to generate and print the table
for i in range(1, range_limit + 1):
    print(f"{number} x {i} = {number * i}")
