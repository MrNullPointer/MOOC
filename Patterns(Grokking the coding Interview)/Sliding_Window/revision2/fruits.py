def fruits_into_baskets(fruits):
    # TODO: Write your code here
    window_start, max_len = 0, 0
    fruits_frequency = dict()

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruits_frequency:
            fruits_frequency[right_fruit] = 0
        fruits_frequency[right_fruit] += 1

        while len(fruits_frequency) > 2:
            left_fruit = fruits[window_start]
            fruits_frequency[left_fruit] -= 1
            if fruits_frequency[left_fruit] == 0:
                del fruits_frequency[left_fruit]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()