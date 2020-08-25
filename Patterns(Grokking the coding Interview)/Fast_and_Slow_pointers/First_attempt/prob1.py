class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    reverse_head = reverse(slow)
    copy_reverse_head = reverse_head

    while reverse_head and head:
        if reverse_head.value != head.value:
            break
        head = head.next
        reverse_head = reverse_head.next
    
    reverse(copy_reverse_head)
    if reverse_head is None or head is None:
        return True
    return False

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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
