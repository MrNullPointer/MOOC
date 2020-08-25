def find_missing_numbers(nums):
    missingNumbers = []
    i, n  = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for idx in range(len(nums)):
        if idx != nums[idx] - 1:
            missingNumbers.append(idx + 1)

    # TODO: Write your code here
    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))

main()