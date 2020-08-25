def fruits_into_baskets(fruits):
    # TODO: Write your code here
    window_start = 0
    fruit_dict = dict()
    max_len = 0
    for window_end in range(len(fruits)):
        fruit_right = fruits[window_end]
        if fruit_right not in fruit_dict:
            fruit_dict[fruit_right] = 0
        fruit_dict[fruit_right] += 1

        while len(fruit_dict) > 2:
            fruit_left = fruits[window_start]
            fruit_dict[fruit_left] -= 1
            if fruit_dict[fruit_left] == 0:
                del fruit_dict[fruit_left]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()