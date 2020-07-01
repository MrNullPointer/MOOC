def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    # Check if we're serving orders first-come, first-served
    
    
    take_out_idx, dine_in_idx = 0, 0
    take_out_length, dine_in_length = len(take_out_orders), len(dine_in_orders)

    for order in served_orders:
        if take_out_idx < take_out_length and take_out_orders[take_out_idx] == order:
            take_out_idx += 1
        elif dine_in_idx < dine_in_length and dine_in_orders[dine_in_idx] == order:
            dine_in_idx += 1
        else:
            return False
    
    if take_out_idx != take_out_length or dine_in_idx != dine_in_length:
        return False
    
    return True

print(is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))

print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5]))

print(is_first_come_first_served([], [2, 3, 6], [2, 3, 6]))

print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5]))

print(is_first_come_first_served([1, 9], [7, 8], [1, 7, 8]))

'''
True
False
True
False
False
'''
