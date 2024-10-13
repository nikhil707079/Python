# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Print the table header
print("Celsius\tFahrenheit")
print("--------------------")

# Loop through Celsius values from 0 to 100
for c in range(0, 101):
    f = celsius_to_fahrenheit(c)
    print(f"{c}\t{f:.1f}")
