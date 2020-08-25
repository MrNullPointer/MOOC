from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        current_ = 0

        for _ in range(n):
            current = queue.popleft()
            current_ += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        current_ /= n
        result.append(current_)


    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
