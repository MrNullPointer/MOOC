def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    
    return nums

def main():
    print(cyclic_sort([3, 1, 0, 4, 2]))
    print(cyclic_sort([2, 0, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 0, 4, 3, 2]))


main()