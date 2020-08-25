class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half_head = reverse(slow)
    second_half_copy = second_half_head

    while head and second_half_head:
        if head.value != second_half_head.value:
            break

        head = head.next
        second_half_head = second_half_head.next
    

    reverse(second_half_copy)
    if head is None or second_half_head is None:
        return True
    
    return False

def reverse(head):
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    
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
