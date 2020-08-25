def find_string_anagrams(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    result_indexes = []

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indexes.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            window_start += 1

    # TODO: Write your code here
    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
