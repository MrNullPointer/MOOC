def find_all_duplicates(nums):
    duplicateNumbers = []
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for idx in range(len(nums)):
        if idx + 1 != nums[idx]:
            duplicateNumbers.append(nums[idx])
    return duplicateNumbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()