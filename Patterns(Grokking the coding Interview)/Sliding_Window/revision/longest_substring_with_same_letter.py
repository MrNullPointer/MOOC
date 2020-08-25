def length_of_longest_substring(str, k):
    # TODO: Write your code here
    window_start, longest_so_far, max_len = 0, 0, 0
    char_frequency = {}

    for window_end in range(len(str)):
        right = str[window_end]
        if right not in char_frequency:
            char_frequency[right] = 0
        char_frequency[right] += 1
        longest_so_far = max(longest_so_far, char_frequency[right])

        if (window_end - window_start + 1) - longest_so_far > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
    print(length_of_longest_substring("aabbaabcaab", 2))


main()
