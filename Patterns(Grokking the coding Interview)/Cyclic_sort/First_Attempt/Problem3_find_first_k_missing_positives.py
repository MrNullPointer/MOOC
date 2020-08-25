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
    
    num = 0
    nums_set = set()

    for idx in range(n):
        if nums[idx] != idx + 1:
            if num < k:
                missingNumbers.append(idx + 1)
                nums_set.add(nums[idx])
                num += 1
    
    idx = 1
    while num < k:
        i += idx
        if i not in nums_set:
            missingNumbers.append(i)
            num += 1
    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()