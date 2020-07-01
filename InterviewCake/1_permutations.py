def has_palindrome_permutation(the_string):
    
    # Check if any permutation of the input is a palindrome
    permute_set = set()

    for char in the_string:
        if char in permute_set:
            permute_set.remove(char)
        else:
            permute_set.add(char)

    return len(permute_set) <= 1



print(has_palindrome_permutation('aabcbcd') ," == True")
print(has_palindrome_permutation('') ," == True")
print(has_palindrome_permutation('a') ," == True")
print(has_palindrome_permutation('aabcd') ," == False")
print(has_palindrome_permutation('aabbcd') ," == False")