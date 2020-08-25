def non_repeat_substring(str):
    # TODO: Write your code here
    window_start, max_subarray = 0, 0
    char_idx = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_idx:
            window_start = max(window_start, char_idx[right_char] + 1)
        char_idx[right_char] = window_end

        max_subarray = max(max_subarray, window_end - window_start + 1)
    return max_subarray


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()