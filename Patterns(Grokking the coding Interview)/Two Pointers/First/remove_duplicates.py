def remove_duplicates(arr):
    # TODO: Write your code here
    next_num = 1
    idx = 1
    while idx < len(arr):
        if (arr[next_num - 1] != arr[idx]):
            arr[next_num] = arr[idx]
            next_num += 1
        idx += 1
    return next_num


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()