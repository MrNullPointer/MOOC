import math


def smallest_subarray_with_given_sum(s, arr):
    start_idx, sum = 0, 0
    min_idx = math.inf

    for idx in range(len(arr)):
        sum += arr[idx]
        while sum >= s:
            min_idx = min(idx, idx - start_idx + 1)
            sum -= arr[start_idx]
            start_idx += 1

    if min_idx == math.inf:
            return 0
    return min_idx


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()