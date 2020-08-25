import math


def triplet_sum_close_to_target(arr, target):
    smallest = math.inf
    arr.sort()

    for idx in range(len(arr) - 2):
        left = idx + 1
        right = len(arr) - 1
        while left < right:
            difference = target - arr[idx] - arr[left] - arr[right]
            if difference == 0:
                return target - difference

            if abs(difference) < abs(smallest) or (abs(difference)
                                                   == abs(smallest)
                                                   and difference > smallest):
                smallest = difference
            if difference > 0:
                left += 1
            else:
                right -= 1

    return target - smallest


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()