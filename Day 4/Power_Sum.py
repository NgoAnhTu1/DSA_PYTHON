def power_sum(array,power=1):
    sum = 0
    for _ in range (len(array)):
        if type(array[_]) is int:
            sum += array[_]
        elif type(array[_]) is list:
            sum += power_sum(array[_],power + 1)
    return sum**power

arr = [2, 3, [4, 1, 2]]
print(power_sum(arr))