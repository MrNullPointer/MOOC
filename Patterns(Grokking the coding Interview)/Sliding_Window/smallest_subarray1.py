import math

def smallest_subarray_with_given_sum(s, arr):
    # TODO: Write your code here
    window_start, sum = 0, 0
    smallest_arr = math.inf

    for window_end in range(len(arr)):
        sum += arr[window_end]

        while sum >= s:
            smallest_arr = min(smallest_arr, window_end - window_start + 1)
            sum -= arr[window_start]
            window_start += 1

    if smallest_arr == math.inf:
        return 0
    return smallest_arr


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()

