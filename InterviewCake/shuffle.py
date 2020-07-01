import random

def get_random(floor, cieling):
    return random.randrange(floor, cieling + 1)


def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    cieling = len(the_list) - 1

    for idx in range(0,len(the_list) - 1):
        rand_idx = get_random(idx, cieling)

        the_list[idx], the_list[rand_idx] = the_list[rand_idx], the_list[idx]
            
    return the_list


sample_list = [100, 12, 65, 8783, 7821, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)