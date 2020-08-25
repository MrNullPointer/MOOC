def find_averages_of_subarrays(k, arr):
    window_start, sum = 0, 0
    result = []

    for window_end in range(len(arr)):
        sum += arr[window_end]
        if window_end >= k - 1:
            result.append(sum / k)
            sum -= arr[window_start]
            window_start += 1

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
