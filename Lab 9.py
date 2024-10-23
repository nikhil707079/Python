def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print(f"The largest number is: {largest}")

# Example usage:
a = 10
b = 25
c = 15
find_largest(a, b, c)
