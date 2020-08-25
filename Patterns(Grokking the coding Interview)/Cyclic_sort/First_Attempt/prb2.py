def find_first_missing_positive(nums):
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
           nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for idx in range(n):
        if nums[idx] != idx + 1 :
            return idx + 1
    return -1


def main():
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))


main()