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

def find_all_paths(current_node, sum, current_path, all_paths):
    if current_node is None:
        return
    
    current_path.append(current_node.val)

    if current_node.val == sum and not current_node.left and not current_node.right:
        all_paths.append(list(current_path))
    
    else:
        find_all_paths(current_node.left, sum - current_node.val, current_path, all_paths)
        find_all_paths(current_node.right, sum - current_node.val, current_path, all_paths)
    
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
