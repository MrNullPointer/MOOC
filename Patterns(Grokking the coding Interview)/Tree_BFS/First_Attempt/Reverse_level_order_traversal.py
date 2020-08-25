from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    # TODO: Write your code here
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        current_result = list()
        for _ in range(n):
            current = queue.popleft()
            current_result.append(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        result.appendleft(current_result)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
