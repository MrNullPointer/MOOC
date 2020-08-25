def find_averages_of_subarrays(k, list_of_ints):
    window_start, sum = 0, 0.0
    result = list()

    for window_end in range(len(list_of_ints)):
        sum += list_of_ints[window_end]
        if window_end - window_start >= k - 1:
            result.append(sum / k)
            sum -= list_of_ints[window_start]
            window_start += 1
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
