#----in this approach we use a dictionary
#----by using dictionary, our space complexity increases


def length_of_longest_substring(arr, k):
    # TODO: Write your code here
    window_start, max_len = 0, 0
    bit_frequency = {}

    for window_end in range(len(arr)):
        right_bit = arr[window_end]
        if right_bit not in bit_frequency:
            bit_frequency[right_bit] = 0
        bit_frequency[right_bit] += 1

        if bit_frequency[0] > k:
            left_bit = arr[window_start]
            bit_frequency[left_bit] -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(
        length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                                    3))

main()