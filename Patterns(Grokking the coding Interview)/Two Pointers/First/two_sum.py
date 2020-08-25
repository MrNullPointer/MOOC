def two_sum(arr, target):
    first = 0
    last = len(arr) - 1
    result = []
    while first < last:
        if arr[first] + arr[last] == target:
            return [first, last]
        if arr[first] + arr[last] < target:
            first += 1
        else:
            last -= 1
    return result


print(two_sum([1,7,13,17,55], 56))