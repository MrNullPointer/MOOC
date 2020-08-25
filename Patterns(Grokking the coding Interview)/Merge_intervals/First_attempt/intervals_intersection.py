def merge(intervals_a, intervals_b):
    a_idx, b_idx, start, end = 0, 0, 0, 1
    result = []

    while a_idx < len(intervals_a) and b_idx < len(intervals_b):
        a_overlaps_b = intervals_a[a_idx][start] >= intervals_b[b_idx][
            start] and intervals_a[a_idx][start] <= intervals_b[b_idx][end]

        b_overlaps_a = intervals_b[b_idx][start] >= intervals_a[a_idx][
            start] and intervals_a[a_idx][end] >= intervals_b[b_idx][start]

        if a_overlaps_b or b_overlaps_a:
            result.append([
                max(intervals_a[a_idx][start], intervals_b[b_idx][start]),
                min(intervals_a[a_idx][end], intervals_b[b_idx][end])
            ])

        if intervals_a[a_idx][end] < intervals_b[b_idx][end]:
            a_idx += 1
        else:
            b_idx += 1

    return result


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()