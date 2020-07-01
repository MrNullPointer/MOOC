def split_words(line):
    words = list()
    curr_start = 0
    curr_length = 0
    
    for idx, char in enumerate(line):
        if char.isalpha():
            if curr_length == 0:
                curr_start = idx
            curr_length += 1
        else:
            if curr_length == 0:
                continue
            word = line[curr_start : curr_start + curr_length]
            words.append(word)
            curr_length = 0
    return words

word_to_counts = {}

def add_word_to_dictionary(word):
    if word in word_to_counts:
        word_to_counts[word] += 1
    else:
        word_to_counts[word] = 1
    




line =   "! After beating the eggs, Dana read the next step:"
print(split_words(line))