from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        for idx in range(n):
            current = queue.popleft()
            if idx == n - 1:
                result.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
