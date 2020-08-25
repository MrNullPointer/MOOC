class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here
    find_all_paths(root, sum, [], allPaths)
    return allPaths

def find_all_paths(current, sum, current_path, all_paths):
    if not current:
        return
    
    current_path.append(current.val)

    if current.val == sum and not current.left and not current.right:
        all_paths.append(list(current_path))
    
    else:
        find_all_paths(current.left, sum - current.val, current_path, all_paths)
        find_all_paths(current.right, sum - current.val, current_path, all_paths)
    
    del current_path[-1]

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " +
          str(find_paths(root, sum)))


main()
