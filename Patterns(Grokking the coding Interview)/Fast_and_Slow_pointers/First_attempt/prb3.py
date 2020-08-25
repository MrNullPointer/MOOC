def circular_array_loop_exists(arr):
    # TODO: Write your code here
    for idx in range(len(arr)):
        slow, fast = idx, idx
        direction = arr[idx] >= 0
        while True:
            slow = find_next_arr(arr, direction, slow)
            fast = find_next_arr(arr, direction, fast)

            if fast != -1:
                fast = find_next_arr(arr, direction, fast)

            if fast == -1 or slow == -1 or fast == slow:
                break
        
        if slow != -1 and fast == slow:
            return True
    
    return False


def find_next_arr(arr, direction, idx):
    curr_direction = arr[idx] >= 0

    if curr_direction != direction:
        return -1
    
    next_idx = (idx + arr[idx]) % len(arr)

    if next_idx == idx:
        return -1
    
    return next_idx


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
