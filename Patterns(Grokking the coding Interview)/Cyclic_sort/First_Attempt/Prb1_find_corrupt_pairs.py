def find_corrupt_numbers(nums):
    # TODO: Write your code here
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for idx in range(len(nums)):
        if idx + 1 != nums[idx]:
            return[nums[idx], idx + 1]

    return [-1, -1]


def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()