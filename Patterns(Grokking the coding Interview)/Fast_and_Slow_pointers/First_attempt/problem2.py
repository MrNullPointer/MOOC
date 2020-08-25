from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    # TODO: Write your code here
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    head_second_half = reverse(slow)
    head_first_half = head

    while head_first_half and head_second_half:
        _next = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = _next

        _next = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = _next

    if head_first_half:
        head_first_half.next = None
    
    return None

def reverse(head):
    prev = None
    
    while head:
        _next = head.next
        head.next = prev
        prev = head
        head = _next
    
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
