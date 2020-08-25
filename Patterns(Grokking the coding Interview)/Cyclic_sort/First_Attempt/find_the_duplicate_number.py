def find_duplicate(nums):
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for idx in range(n):
        if idx != nums[idx] - 1:
            return nums[idx]
    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()