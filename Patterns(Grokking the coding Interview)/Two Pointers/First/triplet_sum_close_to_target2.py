import math as m


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = m.inf

    for idx in range(len(arr) - 2):
        idx_num = arr[idx]
        left = idx + 1
        right = len(arr) - 1
        while left < right:
            left_num = arr[left]
            right_num = arr[right]
            target_diff = target_sum - idx_num - left_num - right_num

            if target_diff == 0:
                return target_sum - target_diff

            if abs(target_diff) < abs(smallest_diff) or (
                    abs(target_diff) == abs(smallest_diff)
                    and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_diff

def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()