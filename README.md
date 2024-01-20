# My python Code Challanges
## Chalange 1: Making Perputul Calender
This Python script is designed to print a calendar for a specific month of a specific year. It consists of several functions:

1. `is_leap_year(year)`: This function checks if a given year is a leap year. A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
2. `print_calendar(year, month, odd_days)`: This function prints the calendar for a given month of a given year. It takes into account the number of odd days to correctly align the dates.
3. `count_odd_days(input_year, input_month)`: This function calculates the number of odd days up to the given month of the given year. This is used to determine the day of the week of the first day of the month.
4. `validate_input(input_year, input_month)`: This function validates the user input for the year and month. If the month is not between 1 and 12, it raises a ValueError.
The script first asks the user to input the year and month. It then validates the input, counts the odd days, and finally prints the calendar.
Please note that this script uses a global dictionary `months` to store the names and number of days of each month. The number of days in February is updated to 29 if the input year is a leap year. 
