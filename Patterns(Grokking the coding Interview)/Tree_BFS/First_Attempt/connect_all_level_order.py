from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    # TODO: Write your code here
    queue = deque()
    queue.append(root)

    prev_elem, curr_elem = None, None

    while queue:
        curr_elem = queue.popleft()
        if prev_elem:
            prev_elem.next = curr_elem
        prev_elem = curr_elem

        if curr_elem.left:
            queue.append(curr_elem.left)
        if curr_elem.right:
            queue.append(curr_elem.right)
            
    return


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
