def cyclic_sort(nums):
    # TODO: Write your code here
    idx = 0
    while idx < len(nums):
        num_idx = nums[idx] - 1
        if nums[num_idx] != nums[idx]:
            nums[num_idx], nums[idx] = nums[idx], nums[num_idx]
        else:
            idx += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()