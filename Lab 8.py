# Function to print factors of a given number
def print_factors(number):
    print(f"Factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Input from the user
num = int(input("Enter a number: "))
print_factors(num)
