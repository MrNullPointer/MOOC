def max_sub_array_of_size_k(k, arr):
    window_start, sum = 0, 0
    max_len = 0

    for window_end in range(len(arr)):
        sum += arr[window_end]
        if window_end - window_start + 1 >= k:
            max_len = max(max_len, sum)
            sum -= arr[window_start]
            window_start += 1

    return max_len


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()