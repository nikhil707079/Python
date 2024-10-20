def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
num_terms = int(input("Enter the number of terms: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    print(fibonacci_series(num_terms))
