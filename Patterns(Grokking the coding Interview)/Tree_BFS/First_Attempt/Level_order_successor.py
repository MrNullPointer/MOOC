from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    # TODO: Write your code here
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)

        for _ in range(n):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            if current.val == key:
                if queue:
                    new_number = queue.popleft()
                    return new_number
                else:
                    return None
    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
