def sort_scores(unsorted_scores, highest_possible_score):
    
    # Sort the scores in O(n) time
    sort_count = [0] * highest_possible_score

    for val in unsorted_scores:
        if sort_count[val]:
            sort_count[val] += 1
        else:
            sort_count[val] = 1
    
    sorted = []
    for idx in range(len(sort_count) - 1, -1, -1):
        count = sort_count[idx]

        for time in range(count):
            sorted.append(idx)

    return sorted

print(sort_scores([], 100))
print(sort_scores([55], 100))
print(sort_scores([30, 60], 100))
print(sort_scores([37, 89, 41, 65, 91, 53], 100))
print(sort_scores([20, 10, 30, 30, 10, 20], 100))
