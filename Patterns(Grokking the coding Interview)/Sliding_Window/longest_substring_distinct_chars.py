def longest_substring_with_k_distinct(str, k):
    # TODO: Write your code here
    window_start = 0
    string_dict = {}
    max_length = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in string_dict:
            string_dict[right_char] = 0
        string_dict[right_char] += 1

        while len(string_dict) > k:
            left_char = str[window_start]
            string_dict[left_char] -= 1
            if string_dict[left_char] == 0:
                del string_dict[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
