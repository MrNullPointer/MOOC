import math

def smallest_subarray_with_given_sum(s, arr):
    # TODO: Write your code here
    start_idx, sum = 0, 0
    min_arr = math.inf
    for end_idx in range(len(arr)):
        sum += arr[end_idx]
        while sum >= s:
            min_arr = min(min_arr, end_idx - start_idx + 1)
            sum -= arr[start_idx]
            start_idx += 1

    if min_arr == math.inf:
        return 0
    return min_arr 


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()