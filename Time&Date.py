from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Format the date and time
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")

print("Current Date:", formatted_date)
print("Current Time:", formatted_time)
