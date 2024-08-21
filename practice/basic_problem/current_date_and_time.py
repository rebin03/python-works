# Import the 'datetime' module to work with date and time
import datetime


# Create a datetime object representing the current date and time
now = datetime.datetime.now()

print("Current date and time : ")

# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))