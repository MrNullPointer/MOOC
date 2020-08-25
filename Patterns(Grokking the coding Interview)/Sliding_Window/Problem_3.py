def find_substring(str1, pattern):
    window_start, str_start, matched = 0, 0, 0
    min_len = len(str1) + 1
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                str_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_len > len(str1):
        return ""
    return str1[str_start:str_start + min_len]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))
    print(find_substring("aabbccbbafgabch", "abc"))


main()
