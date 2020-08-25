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

def find_all_paths(root, sum, current_path, allPaths):
    if root is None:
        return
    
    current_path.append(root.val)

    if root.val == sum and not root.left and not root.right:
        allPaths.append(list(current_path))
    
    else:
        find_all_paths(root.left, sum - root.val, current_path, allPaths)
        find_all_paths(root.right, sum - root.val, current_path, allPaths)
    
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
