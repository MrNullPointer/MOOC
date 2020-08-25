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
    if root is None:
        return
    
    queue = deque()
    queue.append(root)
    idx = 0

    while True:
        n = len(queue)
        if idx == n:
            break
        while idx < n:
            if idx > 0 and queue[idx - 1].next == None:
                queue[idx - 1].next = queue[idx]
            
            if idx == n - 1:
                queue[idx].next = None
            else:
                queue[idx].next = queue[idx + 1]
            
            if queue[idx].left:
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
    connect_all_siblings(root)
    root.print_tree()


main()
