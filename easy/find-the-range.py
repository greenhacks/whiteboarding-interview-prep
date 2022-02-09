"""Given a list of numbers, return the smallest and the largest number.

>>> find_range([3, 4, 2, 5, 10])
(2, 10)

>>> find_range([43, 3, 44, 20, 2, 1, 100])
(1, 100)

For an empty list, it should return None as both smallest and largest:

>>> find_range([])
(None, None)

Make sure it works with a list of one item, which is both smallest and largest:

>>> find_range([7])
(7, 7)
"""

# input: list of nums
# output: tuple with two integers

# pseudocode
# i want to take the list and sort it?
# or do i want to make a set and get the min and max?


# code
def find_the_range(lst):
    result = []
    if lst == []:
        return [None, None]
    else:
        result.append(min(lst))
        result.append(max(lst))

        return result


# test cases
print(find_the_range([0, 20, 4, 1, 3])) # expect [0, 20]
print(find_the_range([3])) # expect [3, 3]
print(find_the_range([])) # expect [None, None]

# edge cases
# empty list returns []
# one item returns the item twice

# runtime: O(n)?
