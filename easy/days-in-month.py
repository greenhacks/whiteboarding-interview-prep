""" Given a string with a month and a year (separated by a space), return the number of days in that month.

Leap years are a bit tricky. A year is a leap year if and only if:

    it is evenly divisible by 4

    except if it is divisible by 100, in which case it isn’t

    except if it is divisible by 400, in which case it is

So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 2000 is divisible by 400, so it was.

"""

# input:  string (June 2019)
# output: integer

# pseudocode
# from calendar import month
# from multiprocessing.sharedctypes import Value


# every month will have the same number of days as every other year
# leap years are the only things to watch out for

# if a year is divisible by 400 then it's a leap year
# if it's divisible by 100 , then it's not a leap year
# if it's divisible by 4, then it's a leap year

# how to translate this to code?

# need to have a dictionary of months and days in month

# split the input string by a space, which returns a list

# if month = february AND year is divisible by 4 or 400,
#     return 29

# else, 
#     loop through the dictionary and return the value of the first index

# code
months = {
    "January": 31, 
    "February": 28, # or 29***
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def get_days_in_month(string):

    split_str = string.split(" ") # returns a list with two elements

    month = split_str[0] 
    year = int(split_str[1])

    if month == "February" and year % 4 == 0 or year % 400 == 0:
        return 29
    
    else:
        if month in months:
            return months[month]

# test cases
print(get_days_in_month("June 2019")) # expect 30
print(get_days_in_month("February 2020")) # expect 29
print(get_days_in_month("February 2019")) # expect 28
# edge cases