def reverse(list_of_strings):
    first_idx = 0
    last_idx = len(list_of_strings) - 1

    while first_idx < last_idx:
        list_of_strings[first_idx], list_of_strings[last_idx] = list_of_strings[last_idx], list_of_strings[first_idx]
        first_idx += 1
        last_idx -= 1
    return list_of_strings

def reverse_words(message):
    
    # Decode the message by reversing the words
    first_idx = 0
    last_idx = len(message) - 1
    message = reverse(message)

    for idx in range(len(message) + 1):
        if idx == len(message) or message[idx] == " ":
            last_idx = idx
            message[first_idx:last_idx] = reverse(message[first_idx:last_idx])
            first_idx = idx + 1
    # message[first_idx:] = reverse(message[first_idx:])
    return message


message = list('vault')
print(reverse_words(message))
print(list('vault'))


message = list('thief cake')
print(reverse_words(message))
print(list('cake thief'))


message = list('')
print(reverse_words(message))
print(list(''))