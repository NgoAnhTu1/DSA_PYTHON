"""
Two Sum - You are given an array of Integers and another integer targetValue. 
Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue
"""

def two_sum(array,target):
    if len(array) <= 1:
        return []
    
    hash_table = {}
    for i in range(len(array)):
        tmp = target - array[i]
        if tmp in hash_table:
            return [hash_table[tmp], i]
        hash_table[array[i]] = i
    return []


array = [3, 1, 5, 7, 8]
print(two_sum(array, 12))
