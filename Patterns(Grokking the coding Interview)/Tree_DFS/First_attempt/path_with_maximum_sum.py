import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        # TODO: Write your code here
        self.max_sum = -math.inf
        self.max_path_sum(root)
        return self.max_sum
    
    def max_path_sum(self, current_node):
        if current_node is None:
            return 0
        
        left_sum = self.max_path_sum(current_node.left)
        right_sum = self.max_path_sum(current_node.right)

        left_sum = max(left_sum, 0)
        right_sum = max(right_sum, 0)

        current_sum = left_sum + right_sum + current_node.val
        self.max_sum = max(self.max_sum, current_sum)

        return max(left_sum, right_sum) + current_node.val



def main():
    maximumPathSum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " +
          str(maximumPathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " +
          str(maximumPathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " +
          str(maximumPathSum.find_maximum_path_sum(root)))


main()
