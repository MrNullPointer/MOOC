def merge_lists(my_list, alices_list):
    
    # Combine the sorted lists into one large sorted list
    sorted_size = len(my_list) + len(alices_list)
    sorted_list = [None] * sorted_size

    left_idx, right_idx, sorted_idx = 0, 0, 0

    while sorted_idx < sorted_size:
        is_my_list = left_idx < len(my_list)
        is_alice_list = right_idx < len(alices_list)

        if (is_my_list and (not is_alice_list or alices_list[right_idx] > my_list[left_idx])):
            sorted_list[sorted_idx] = my_list[left_idx]
            left_idx += 1
        else:
            sorted_list[sorted_idx] = alices_list[right_idx]
            right_idx += 1
        
        sorted_idx += 1

    return sorted_list



my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_lists(my_list, alices_list))

print(merge_lists([5, 6, 7], []))
expected = [5, 6, 7]