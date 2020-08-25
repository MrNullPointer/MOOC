# def jar(count, nums):
#     candy1, candy2 = 0, 0

#     for count in nums:
#         temp = max(count + candy1, candy2)
#         candy1 = candy2
#         candy2 = temp
#     return candy2


# print(jar(5, [5, 78, 90, 80, 10]))
# print(jar(7, [12, 45, 0, 87, 0, 46, 90]))

# def lastwords(words):
#     if words is None:
#         return
    
#     first_letter = words[-1]
#     second_last = words[-2]

#     return second_last + " " + first_letter

# print(lastwords("Apple"))

