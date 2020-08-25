def find_all_duplicates(nums):
    duplicateNumbers = []
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            else:
                duplicateNumbers.append(nums[i])
                i += 1
        else:
            i += 1
    return duplicateNumbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
