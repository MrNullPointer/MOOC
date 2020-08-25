def find_average(k, arr):
    result = []
    window_start, window_sum = 0, 0.0

    for idx in range(len(arr)):
        window_sum += arr[idx]
        if idx >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return result

print(find_average(2,[1,2,3,4,5]))