def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    num_set = set()
    num_count = 0

    for idx in range(len(nums)):
        if num_count < k:
            if nums[idx] != idx + 1:
                missingNumbers.append(idx + 1)
                num_set.add(nums[idx])
                num_count += 1
    
    x = len(nums)
    curr_idx = 1

    while num_count < k:
        x = x + curr_idx
        if x not in num_set:
            missingNumbers.append(x)
            num_count += 1
        
        #curr_idx += 1

    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()