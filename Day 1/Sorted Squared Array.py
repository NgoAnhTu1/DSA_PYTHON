
"""You are given an array of Integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order."""


def sorted_squared(array): 
    n = len(array)
    right = n - 1
    left = 0
    result = [0] * n
    for i in range (n - 1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] ** 2
            left += 1
        else:
            result[i] = array[right] ** 2
            right -= 1
    return result
array = [-4, -1, 2, 3]
print(sorted_squared(array))