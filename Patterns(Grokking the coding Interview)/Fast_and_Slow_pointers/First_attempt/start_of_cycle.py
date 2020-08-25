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
    while fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = find_len(slow)
            break
    
    return find_start(length, head)

def find_len(slow):
    curr = slow
    length = 0
    while True:
        curr = curr.next
        length += 1
        if curr == slow:
            return length


def find_start(length, head):
    slow, fast = head, head
    while length > 0:
        fast = fast.next
        length -= 1
    
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


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
