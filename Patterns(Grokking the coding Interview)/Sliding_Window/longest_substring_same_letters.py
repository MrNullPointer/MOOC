def length_of_longest_substring(str, k):
    # TODO: Write your code here
    window_start, max_len, max_char_count = 0, 0, 0
    char_frequency = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        max_char_count = max(max_char_count, char_frequency[right_char])

        while ((window_end - window_start + 1) - max_char_count) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            window_start += 1
        
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
    print(length_of_longest_substring("abbbcbbaabca", 1))


main()