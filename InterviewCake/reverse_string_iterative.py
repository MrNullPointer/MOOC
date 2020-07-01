def reverse(list_of_chars):
    
    first_idx = 0
    last_idx = len(list_of_chars) - 1

    while first_idx < last_idx:
        list_of_chars[first_idx],list_of_chars[last_idx] = \
        list_of_chars[last_idx], list_of_chars[first_idx]
        first_idx += 1
        last_idx -= 1
    return list_of_chars



list_of_chars = ['A', 'B', 'C', 'D', 'E']
print(reverse(list_of_chars))
expected = ['E', 'D', 'C', 'B', 'A']

list_of_chars = ['A']
print(reverse(list_of_chars))
expected = ['A']

list_of_chars = []
print(reverse(list_of_chars))
expected = []