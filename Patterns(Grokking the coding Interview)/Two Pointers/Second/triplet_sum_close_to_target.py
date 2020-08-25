import math

def triplet_sum_close_to_target(arr, target_sum):
    # TODO: Write your code here
    smallest_diff = math.inf
    arr.sort()
    for idx in range(len(arr)):
        left = idx + 1
        right = len(arr) - 1
        while left < right:
            curr_diff = target_sum - arr[idx] - arr[left] - arr[right]
            if curr_diff == 0:
                return  target_sum
            
            if abs(smallest_diff) > abs(curr_diff) or (abs(curr_diff) == abs(smallest_diff) and curr_diff > smallest_diff):
                smallest_diff = curr_diff
            
            if curr_diff < 0:
                right -= 1
            else:
                left += 1
    return target_sum - smallest_diff      


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()