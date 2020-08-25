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


def reverse_sub_list(head, p, q):
    # TODO: Write your code here
    _prev, _head = None, head
    i = 0

    while _head and i < p - 1:
        _prev = _head
        _head = _head.next
        i += 1

    end_first_part = _prev
    end_sub_array = _head

    _next = None

    i = 0

    while _head and i < q - p + 1:
        _next = _head.next
        _head.next = _prev
        _prev = _head
        _head = _next
        i += 1
    
    if end_first_part:
        end_first_part.next = _prev
    else:
        head = _prev
    
    end_sub_array.next = _head
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
