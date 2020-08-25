class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    # TODO: Write your code here
    return count_path_sum(root, S, [])


def count_path_sum(current_node, sum, current_list):
    if current_node is None:
        return 0

    current_list.append(current_node.val)
    path_sum, path_count = 0, 0

    for idx in range(len(current_list) - 1, -1, -1):
        path_sum += current_list[idx]

        if path_sum == sum:
            path_count += 1

    path_count += count_path_sum(current_node.left, sum, current_list)
    path_count += count_path_sum(current_node.right, sum, current_list)

    del current_list[-1]

    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
