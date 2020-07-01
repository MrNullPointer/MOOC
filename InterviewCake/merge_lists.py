def merge_lists(my_list, alices_list):
    
    # Combine the sorted lists into one large sorted list
    sorted_list = []
    left_idx, right_idx = 0, 0

    while left_idx < len(my_list) and right_idx < len(alices_list):
        if my_list[left_idx] <= alices_list[right_idx]:
            sorted_list.append(my_list[left_idx])
            left_idx += 1
        else:
            sorted_list.append(alices_list[right_idx])
            right_idx += 1
    
    sorted_list.extend(my_list[left_idx:])
    sorted_list.extend(alices_list[right_idx:])


    return sorted_list



my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))

print(merge_lists([5, 6, 7], []))
expected = [5, 6, 7]