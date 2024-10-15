# Function to determine if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Read an integer value from the user
year = int(input("Enter a year: "))

# Check and print whether the year is a leap year
if is_leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")
