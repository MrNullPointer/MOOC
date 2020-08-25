def find_missing_number(nums):
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    
    for idx in range(n):
        if idx != nums[idx]:
            return idx
    return -1

def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()