def length_of_longest_substring(str, k):
    # TODO: Write your code here
    window_start, max_letter_count, max_length = 0, 0, 0
    char_freq = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        max_letter_count = max(max_letter_count, char_freq[right_char])

        if (((window_end - window_start + 1) - max_letter_count) > k):
            left_char = str[window_start]
            char_freq[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length



def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
    print(length_of_longest_substring("abbbcbbaabca", 1))
    print(length_of_longest_substring("abcdefbb", 2))
    print(length_of_longest_substring("", 2))


main()
