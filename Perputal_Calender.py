# A dictionary to store the names and number of days in each month
months = {1: ("Jan", 31), 2: ("Feb", 28), 3: ("Mar", 31), 4: ("Apr", 30), 5: ("May", 31), 6: ("June", 30), 7: ("July", 31), 8: ("Aug", 31), 9: ("Sep", 30), 10: ("Oct", 31), 11: ("Nov", 30), 12: ("Dec", 31)}

# Function to check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Function to print the calendar for a given month of a given year
def print_calendar(year, month, odd_days):
    print("\n\n        -", months[month][0], year, "-")
    print("Mon Tue Wed Thu Fri Sat Sun")
    # Generate a list of dates for the month
    dates = [str(i).zfill(2) for i in range(1, months[month][1] + 1)]
    # Add spaces for the odd days at the beginning of the month
    lst = ["   "] * (odd_days - 1) + [date + " " for date in dates]
    # Print the dates in a format of a calendar
    for i in range(0, len(lst), 7):
        print(' '.join(lst[i:i+7]))

# Function to count the number of odd days up to the given month of the given year
def count_odd_days(input_year, input_month):
    counting_years = ((input_year - 1) % 400)
    no_of_leap_year = int(counting_years / 4)
    no_of_ordinary_year = counting_years - no_of_leap_year
    # Adjust the days for February if it's a leap year
    if is_leap_year(input_year) and input_month > 2:
        odd_days = ((no_of_leap_year * 2) + no_of_ordinary_year + sum([months[i][1] for i in range(1, input_month)])) + 2
    else:
        odd_days = ((no_of_leap_year * 2) + no_of_ordinary_year + sum([months[i][1] for i in range(1, input_month)])) + 1
    return odd_days % 7

# Function to validate the user input for the year and month
def validate_input(input_year, input_month):
    if input_month > 12 or input_month < 1:
        raise ValueError("Error: Include month properly")

# Inputs
input_year = int(input('Input Year: '))
input_month = int(input('Input month: '))
# Validate the input
validate_input(input_year, input_month)
# Update the number of days in February if it's a leap year
if is_leap_year(input_year):
    months[2] = ("Feb", 29)
# Count the odd days
odd_days = count_odd_days(input_year, input_month)
# Print the calendar
print_calendar(input_year, input_month, odd_days)
