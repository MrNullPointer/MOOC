def search_triplets(arr):
    triplets = []
    # TODO: Write your code here
    arr.sort()
    for idx in range(len(arr)):
        if idx > 0 and arr[idx] == arr[idx - 1]:
            continue
        left_idx = idx + 1
        right_idx = len(arr) - 1
        target = arr[idx]
        while left_idx < right_idx:
            left = arr[left_idx]
            right = arr[right_idx]
            curr_sum = left + right
            if target + curr_sum == 0:
                triplets.append([target, left, right])
                left_idx += 1
                right_idx -= 1
                while left == arr[left_idx]:
                    left_idx += 1
                while right == arr[right_idx]:
                    right_idx -= 1
            elif curr_sum + target < 0:
                left_idx += 1
            else:
                right_idx -= 1
    return triplets


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([-5, 2, -1, -2, 3, -1, -2, -2, -2, -2]))
    print(search_triplets([-5, 2, -1, -2, 3, -1, -2, -2, -2, -2, 3, 2]))


main()