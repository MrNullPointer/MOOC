def remove_element(arr, key):
    next_elem = 0
    for idx in range(len(arr)):
        if arr[idx] != key:
            arr[next_elem] = arr[idx]
            next_elem += 1
    return next_elem


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " + str(remove_element([2, 11, 2, 2, 1], 2)))


main()
