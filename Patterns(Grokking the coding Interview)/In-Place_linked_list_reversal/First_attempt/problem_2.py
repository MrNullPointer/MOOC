from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    # TODO: Write your code here
    last, num_elements = head, 1

    while last.next:
        last = last.next
        num_elements += 1
    
    last.next = head
    rotations %= num_elements
    skip_idx = num_elements - rotations

    last_sub_array = head

    for idx in range(skip_idx - 1):
        last_sub_array = last_sub_array.next
    
    head = last_sub_array.next
    last_sub_array.next = None
    
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
