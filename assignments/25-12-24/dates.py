# Python Dates
# A date in Python is not a built-in data type of its own, but we can use the datetime module to work with dates.

# Importing the datetime module to work with dates as date objects:
import datetime

# Example: Display the current date and time:
x = datetime.datetime.now()  # Get current date and time
print(x)  # Prints current date and time like '2025-01-03 16:36:40.351575'

# Date Output Explanation:
# The datetime object contains:
# - Year
# - Month
# - Day
# - Hour
# - Minute
# - Second
# - Microsecond

# The datetime module has many methods to return information about the date object.
# Below are a few examples:

# Example: Return the year and the name of the weekday:
import datetime

x = datetime.datetime.now()  # Get current date and time

print(x.year)  # Get the year part of the current date
print(x.strftime("%A"))  # Get the full name of the weekday (e.g., 'Friday')

# Creating Date Objects:
# To create a date object, we use the datetime() class (constructor) from the datetime module.

# Example: Create a date object with year, month, and day:
import datetime

x = datetime.datetime(2020, 5, 17)  # Create a datetime object for May 17, 2020
print(x)  # Prints the created date: '2020-05-17 00:00:00'

# Additional Parameters in datetime() class:
# The datetime() class can also take parameters for time and timezone, but they are optional:
# - Hour
# - Minute
# - Second
# - Microsecond
# - Timezone (None by default)

# The strftime() Method:
# The datetime object has a method called strftime() to format date objects into readable strings.
# The method takes one parameter, the format, to specify how the string should look.

# Example: Display the full name of the month:
import datetime

x = datetime.datetime(2018, 6, 1)  # Create a datetime object for June 1, 2018

print(x.strftime("%B"))  # Format and print the full name of the month: 'June'

# Legal format codes for strftime():
# Here is a list of commonly used directives (format codes) for strftime():

# %a - Weekday, short version (e.g., 'Wed')
# %A - Weekday, full version (e.g., 'Wednesday')
# %w - Weekday as a number (0-6, 0 is Sunday)
# %d - Day of the month (01-31)
# %b - Month name, short version (e.g., 'Dec')
# %B - Month name, full version (e.g., 'December')
# %m - Month as a number (01-12)
# %y - Year, short version, without century (e.g., '18')
# %Y - Year, full version (e.g., '2018')
# %H - Hour (00-23)
# %I - Hour (00-12)
# %p - AM/PM
# %M - Minute (00-59)
# %S - Second (00-59)
# %f - Microsecond (000000-999999)
# %z - UTC offset (e.g., '+0100')
# %Z - Timezone (e.g., 'CST')
# %j - Day number of the year (001-366)
# %U - Week number of the year (00-53, Sunday as the first day of the week)
# %W - Week number of the year (00-53, Monday as the first day of the week)
# %c - Local version of date and time (e.g., 'Mon Dec 31 17:41:00 2018')
# %C - Century (e.g., '20')
# %x - Local version of date (e.g., '12/31/18')
# %X - Local version of time (e.g., '17:41:00')
# %% - A % character
# %G - ISO 8601 year (e.g., '2018')
# %u - ISO 8601 weekday (1-7)
# %V - ISO 8601 week number (01-53)

# Exercise:
# The task is to determine which syntax will print the current date.
import datetime
x = datetime.datetime  # Importing datetime class from datetime module

# Which of these will print the current date?

# Option 1: Invalid syntax, no method `datetime()` for the datetime class
print(x.datetime())  # This will raise an error: 'datetime' object has no attribute 'datetime'

# Option 2: Prints just the date (not time)
print(x.date())  # Will not work because x is the datetime class, not an instance of datetime object

# Option 3: Correct syntax, prints the current date and time
print(x.now())  # This will print the current date and time (e.g., '2025-01-03 16:36:40')
