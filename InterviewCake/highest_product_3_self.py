def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError("Less than three numbers!!")

    # Calculate the highest product of three numbers
    high = max(list_of_ints[0], list_of_ints[1])
    low = min(list_of_ints[0], list_of_ints[1])
    highest_2 = list_of_ints[0] * list_of_ints[1]
    lowest_2 = list_of_ints[0] * list_of_ints[1]
    highest_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for idx in range(2,len(list_of_ints)):
        curr = list_of_ints[idx]

        highest_3 = max(highest_3, highest_2 * curr, lowest_2 * curr)

        highest_2 = max(curr * high, low * curr, highest_2)
        lowest_2 = min(curr * low, curr * high, lowest_2)

        high = max(high, curr)
        low = min(low, curr)
    return highest_3


print(highest_product_of_3([1, 2, 3, 4]))
print(highest_product_of_3([-5, -1, -3, -2]))
print(highest_product_of_3([6, 1, 3, 5, 7, 8, 2]))
print(highest_product_of_3([-5, 4, 8, 2, 3]))
print(highest_product_of_3([-10, 1, 3, 2, -10]))

