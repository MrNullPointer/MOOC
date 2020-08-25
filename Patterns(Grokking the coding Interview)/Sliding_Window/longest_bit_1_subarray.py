def length_of_longest_substring(arr, k):
    # TODO: Write your code here
    window_start, max_len_1, max_len = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_len_1 += 1
        if (window_end - window_start + 1) - max_len_1 > k:
            if arr[window_start] == 1:
                max_len_1 -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(
        length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                                    3))

main()