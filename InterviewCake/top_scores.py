def sort_scores(unsorted_scores, highest_possible_score):
    
    # Sort the scores in O(n) time
    the_list = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        the_list[score] += 1
    
    sorted_scores = []

    for idx in range(highest_possible_score, -1 , -1):

        count = the_list[idx]
        for val in range(count):
            sorted_scores.append(idx)

    return sorted_scores


print(sort_scores([], 100))
print(sort_scores([55], 100))
print(sort_scores([30, 60], 100))
print(sort_scores([37, 89, 41, 65, 91, 53], 100))
print(sort_scores([20, 10, 30, 30, 10, 20], 100))