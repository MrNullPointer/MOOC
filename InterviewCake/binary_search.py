def binary_search(nums, target):
    floor = -1
    cieling = len(nums)

    while floor + 1 < cieling:
        distance = cieling - floor
        half_distance = distance // 2
        guess_idx = floor + half_distance
        guess_number = nums[guess_idx]

        if target == guess_number:
            return True
        if target < guess_number:
            cieling = guess_idx
        else:
            floor = guess_idx
    return False


print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 1))
print(binary_search([1,2,3,4,5,6], 32))