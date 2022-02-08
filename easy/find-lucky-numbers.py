"""Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

You can trust that this function will never be called with n < 0 or n > 10.

For example:

>>> lucky_numbers(2)
[3, 7]

It’s legal to ask for no numbers:

>>> lucky_numbers(0)
[]

And if we ask for all numbers, we shouldn’t get any repeats:

>>> sorted(lucky_numbers(10))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

# input: integer
# output: list


# pseudocode

# the argument will give the number of elements in the list
# we need to use a random integer method?
# are we allowed to import the random module?
# we essentially want to get n number of random integers and push them to a result variable?


# code
import random

def find_lucky_nums(num):
    # make a range from 0 to 10
    nums = range(1, 11)
     
    # make an empty result variable
    result = []

    # make an index that is equal to the starting number
    index = num

    # while the index is greater than or equal to zero and less than 10
    while index > 0 and index < 10:
        if num == 0:
            return []

        else:
            # create a lucky_num var and append
            lucky_num = result.append(random.choice(nums))
            index -= 1

    return result

# test cases
print(find_lucky_nums(3)) # expect list with three elements
print(find_lucky_nums(0)) # expect []
print(find_lucky_nums(5)) # expect list with five elements

# edge cases