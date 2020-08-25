def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    seen = {}
    for idx, num in enumerate(arr):
        diff = target_sum - num
        if diff in seen:
            return [seen[diff], idx]
        seen[num] = idx
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()