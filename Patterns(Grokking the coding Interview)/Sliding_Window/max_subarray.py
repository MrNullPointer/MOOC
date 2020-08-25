def max_sub_array_of_size_k(k, arr):
      # TODO: Write your code here
    start_idx, max_sub, running_sum = 0, 0, 0
    for idx in range(len(arr)):
          running_sum += arr[idx]
          if idx >= k - 1:
              max_sub = max(max_sub, running_sum)
              running_sum -= arr[start_idx]
              start_idx += 1
    return max_sub

print(max_sub_array_of_size_k(3, [2,1,5,1,3,2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))