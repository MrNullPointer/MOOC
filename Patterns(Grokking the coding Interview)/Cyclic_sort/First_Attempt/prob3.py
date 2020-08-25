def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missing_numbers = list()
    nums_set = set()

    for idx in range(n):
        if len(missing_numbers) < k:
            if nums[idx] != idx + 1:
                missing_numbers.append(idx + 1)
                nums_set.add(nums[idx])
    
    while len(missing_numbers) < k:
        n += 1
        if n not in nums_set:
            missing_numbers.append(n)

    return missing_numbers

def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()