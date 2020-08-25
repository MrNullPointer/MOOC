from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    from_left_to_right = True

    while queue:
        n = len(queue)
        current_list = deque()

        for _ in range(n):
            current = queue.popleft()
            if from_left_to_right:
                current_list.append(current.val)
            else:
                current_list.appendleft(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(current_list)
        from_left_to_right = not from_left_to_right

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
