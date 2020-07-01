
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    if len(served_orders) < len(take_out_orders) + len(dine_in_orders):
        return False
    
    total_orders = len(take_out_orders) + len(dine_in_orders)
    take_out_idx, dine_in_idx, served_idx = 0, 0, 0

    while served_idx < total_orders:
        is_take_out = take_out_idx < len(take_out_orders)
        is_dine_in = dine_in_idx < len(dine_in_orders)

        order = served_orders[served_idx]

        if (is_take_out and order == take_out_orders[take_out_idx]):
            take_out_idx += 1
        elif (is_dine_in and order == dine_in_orders[dine_in_idx]):
            dine_in_idx += 1
        else:
            return False
        
        served_idx += 1
    
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