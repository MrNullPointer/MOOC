def reverse(list_of_chars):
    
    # Reverse the input list of chars in place
    if len(list_of_chars) <= 1:
        return list_of_chars

    first_char = list_of_chars[0]
    last_char = reverse(list_of_chars[1:])
    last_char.append(first_char)
    return last_char 



list_of_chars = ['A', 'B', 'C', 'D', 'E']
print(reverse(list_of_chars))
expected = ['E', 'D', 'C', 'B', 'A']

list_of_chars = ['A']
print(reverse(list_of_chars))
expected = ['A']

list_of_chars = []
print(reverse(list_of_chars))
expected = []