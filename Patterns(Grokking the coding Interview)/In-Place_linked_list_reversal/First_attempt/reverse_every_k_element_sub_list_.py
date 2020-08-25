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


def reverse_every_k_elements(head, k):
    # TODO: Write your code here
    _prev, current = None, head

    while True:
        end_of_first_part = _prev
        end_of_sub_array = current

        i = 0
        _next = None

        while current and i < k:
            _next = current.next
            current.next = _prev
            _prev = current
            current = _next
            i += 1
        
        if end_of_first_part:
            end_of_first_part.next = _prev
        else:
            head = _prev
        
        end_of_sub_array.next = current

        if current is None:
            break

        _prev = end_of_sub_array

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
