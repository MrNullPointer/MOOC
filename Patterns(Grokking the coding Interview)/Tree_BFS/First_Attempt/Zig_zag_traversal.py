from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    is_left = True
    queue = deque()
    if root is None:
        return result
    
    queue.append(root)
    go_left = False

    while queue:
        n = len(queue)
        current_result = deque()

        for _ in range(n):
            current = queue.popleft()

            if go_left:
                current_result.appendleft(current.val)
            else:
                current_result.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:    
                queue.append(current.right)

        result.append(current_result)
        if go_left is True:
            go_left = False
        else:
            go_left = True
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
