from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    # TODO: Write your code here
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)

    min_depth = 0

    while queue:
        n = len(queue)
        min_depth += 1

        for _ in range(n):
            current = queue.popleft()

            if not current.left and not current.right:
                return min_depth
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        

    return -1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
