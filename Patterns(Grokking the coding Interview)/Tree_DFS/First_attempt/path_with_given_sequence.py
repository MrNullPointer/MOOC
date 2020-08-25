class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    # TODO: Write your code here
    count = 0
    return find_one_path(root, sequence, count)


def find_one_path(current, sequence, count):
    if current is None:
        return False

    if sequence[
            count] != current.val:  # cover the edge case where the index grows more than the length of sequence i.e. count >= len(sequence)
        return False

    if count == len(
            sequence) - 1 and current.left is None and current.right is None:
        return True
    count += 1

    return find_one_path(current.left, sequence, count) or find_one_path(
        current.right, sequence, count)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
