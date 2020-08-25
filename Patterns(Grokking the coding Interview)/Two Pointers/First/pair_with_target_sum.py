def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    first = 0
    last = len(arr) - 1
    while first < last:
        sum = arr[first] + arr[last]
        if sum == target_sum:
            return [first, last]

        if sum < target_sum:
            first += 1
        else:
            last -= 1

    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()