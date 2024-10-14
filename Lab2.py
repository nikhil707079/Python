import math

# Print the table header
print("  x   \t  sin(x)  \t  cos(x)  \t  tan(x)")
print("-------------------------------------------")

# Loop through values of x from 0 to 10 with a step of 0.2
x = 0
while x <= 10:
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    tan_x = math.tan(x)
    print(f"{x:.1f}  \t {sin_x:.4f} \t {cos_x:.4f} \t {tan_x:.4f}")
    x += 0.2
