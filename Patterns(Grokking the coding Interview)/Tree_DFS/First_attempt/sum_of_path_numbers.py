class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return sum_of_paths(root, 0)

def sum_of_paths(current, path_sum):
    if current is None:
        return 0
    
    path_sum = 10 * path_sum + current.val

    if current.left is None and current.right is None:
        return path_sum
    
    return sum_of_paths(current.left, path_sum) + sum_of_paths(current.right, path_sum)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
