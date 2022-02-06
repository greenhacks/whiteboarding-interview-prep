"""Given list of ints, return True if any two nums in list sum to 0.

# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True

# Given the wording of our problem, a zero in the list will always 
# make this true, since “any two numbers” could include that same 
# zero for both numbers, and they sum to zero:

# >>> add_to_zero([0, 1, 2])
# True
"""

# input: list of int
# output: Boolean (True or False)

# pseudocode

# write a function that takes in a list
# change the list to a set to remove dupes
# loop through the set

# for each num in the set

#     if negative num in list, 
#     return true

# else return false

# edge cases;
# empty list or zero 


# code
def add_to_zero(lst):
    nums = set(lst)

    for num in nums:
        if -num in nums:
            return True

    return False

# test cases: provided

print(add_to_zero([3, -3, 4, 2, 3])) # True
print(add_to_zero([3, 3, 4, 2, 3])) # False