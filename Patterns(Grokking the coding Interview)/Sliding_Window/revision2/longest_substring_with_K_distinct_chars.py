def longest_substring_with_k_distinct(str, k):
    # TODO: Write your code here
    window_start, max_len = 0, 0
    char_frequency = dict()

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
