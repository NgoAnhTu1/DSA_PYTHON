"""Given an array, rotate the array to the right by k steps, where k is non-negative."""

# Solution 1

# def rotate_array(array, k):
    # if len(array) == 0 or k % len(array) == 0:
    #     return array
    # k = k % len(array)
    # result_array = [0] * len(array)
    # index = 0 
    # for i in range (len(array) -k , len(array)):
    #     result_array[index] = array[i]
    #     index += 1

    # for i in range (0, len(array)-k ):
    #     result_array[index] = array[i]
    #     index += 1
    # return result_array

# Solution 2

def reverse_array(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

def rotate_array(array, k):
    if len(array) == 0 or k % len(array) == 0:
        return array
    k = k % len(array)
    reverse_array(array, 0, len(array) - 1)
    reverse_array(array, 0, k - 1)
    reverse_array(array, k, len(array) - 1)
    return array

# print (rotate_array([1,2,3,4,5,6,7], 10))