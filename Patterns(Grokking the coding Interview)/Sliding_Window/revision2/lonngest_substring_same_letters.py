def length_of_longest_substring(str, k):
    # TODO: Write your code here
    window_start, max_len = 0, 0
    char_max = 0
    char_frequency = dict()
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        char_max = max(char_max, char_frequency[right_char])
        if (window_end - window_start + 1 - char_max) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
