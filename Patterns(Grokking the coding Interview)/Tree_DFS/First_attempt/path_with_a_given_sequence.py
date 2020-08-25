class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    # TODO: Write your code here
    return find_path_sequence(root, sequence, 0)


def find_path_sequence(current_node, sequence, idx):
    if current_node is None:
        return False

    if idx >= len(sequence) or current_node.val != sequence[idx]:
        return False

    if current_node.left is None and current_node.right is None and idx == len(
            sequence) - 1:
        return True

    return find_path_sequence(current_node.left, sequence,
                              idx + 1) or find_path_sequence(
                                  current_node.right, sequence, idx + 1)


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
