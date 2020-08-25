from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_maximum_depth(root):
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    max_len = 0

    while queue:
        n = len(queue)
        max_len += 1

        for _ in range(n):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return max_len



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()