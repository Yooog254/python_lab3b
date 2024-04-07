# declaring the constants.
SECONDS_PER_DAY = 24 * 60 * 60  # Number of seconds in a day
SECONDS_PER_HOUR = 60 * 60      # Number of seconds in an hour

# Input from user
number_of_seconds = int(input("Enter the number of seconds: "))

# Calculations
number_of_days = number_of_seconds // SECONDS_PER_DAY  # Calculate number of days
remaining_seconds = number_of_seconds % SECONDS_PER_DAY  # Calculate remaining seconds after calculating days

number_of_hours = remaining_seconds // SECONDS_PER_HOUR  # Calculate number of hours
remaining_seconds = remaining_seconds % SECONDS_PER_HOUR  # Calculate remaining seconds after calculating hours
number_of_minutes = remaining_seconds // 60  # Calculate number of minutes

# Print results
print(f"{number_of_seconds} seconds is equivalent to:")
print(f"{number_of_days} days, {number_of_hours} hours, and {number_of_minutes} minutes.")
