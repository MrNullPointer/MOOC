from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    # TODO: Write your code here
    fast, slow = head, head
    circle_length = 0
    while fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            circle_length = find_circle_length(slow)
            break

    return find_start(head, circle_length)

def find_circle_length(slow):
    curr = slow
    length = 0
    while True:
        curr = curr.next
        length += 1
        if curr == slow:
            return length


def find_start(head, circle_length):
    pointer1, pointer2 = head, head

    while circle_length > 0:
        pointer2 = pointer2.next
        circle_length -= 1
    
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
