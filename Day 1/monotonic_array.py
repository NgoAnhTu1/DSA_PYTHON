"""An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise."""


def monotonic_array(array):
    array_check = [0] * (len(array) - 1)
    for i in range (len(array_check) ):
        array_check[i] = array[i + 1] - array[i]
    check_incr = check_des =  1
    for i in range(len(array_check)):
        if array_check[i] > 0 : check_des = 0
        if array_check[i] < 0 : check_incr = 0
    if check_incr == 0 and check_des == 0 : return False
    else : return True

array = [-2, 0,1,2,3]
array2 = [5,4,3,2,1, -9]
array3 = [1,5,-1, 5]
print(monotonic_array(array))
print(monotonic_array(array2))
print(monotonic_array(array3)) 