from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    # TODO: Write your code here
    if root is None:
        return

    queue = deque()
    queue.append(root)
    idx = 0

    while True:
        n = (len(queue) - idx) + idx
        if idx >= n:
            break

        while idx < n:
            if idx == n - 1:
                queue[idx].next = None

            else:
                queue[idx].next = queue[idx + 1]

            if (queue[idx].left):
                queue.append(queue[idx].left)
            if queue[idx].right:
                queue.append(queue[idx].right)

            idx += 1



    return


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
