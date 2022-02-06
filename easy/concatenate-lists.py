"""Given two lists. concatenate them (that is, combine them into a single list).

For example, given [1, 2] and [3, 4]:

>>> concat_lists([1, 2], [3, 4])
[1, 2, 3, 4]

It should work if either list is empty:

>>> concat_lists([], [1, 2])
[1, 2]

>>> concat_lists([1, 2], [])
[1, 2]

>>> concat_lists([], [])
[]

"""

# input: two lists
# output: one list

# pseudocode:
# we need a result list to push everything to
# the items need to be in the order they were received

# [3, 6] and [8, 4] will result in [3, 6, 8, 4]

# how do you concatenate? 

# do you just assign a variable to the argument?



# code:
def concat_lists(lst1, lst2):

    new_lst = lst1 + lst2

    return new_lst

# test cases:
print(concat_lists([3, 8], [8, 6])) # expect [3 ,8, 8, 6]
print(concat_lists([], [8, 6])) # expect [8, 6]

# edge cases:


# runtime: O(n)?