# Use this class as the nodes in your linked list
##### Do this again




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    if list1 is None: return list2
    if list2 is None: return list1

    merged_list = LinkedList(None)
    node1 = list1.head
    node2 = list1.head
    
    while node1 is not None or node2 is not None:
        if node1 is None:
            merged_list.append(node2)
            node2 = node2.next
        elif node2 is None:
            merged_list.append(node1)
            node1 = node1.next
        elif node1.value >= node2.value:
            merged_list.append(node2)
            node2 = node2.next
        else:
            merged_list.append(node1)
            node1 = node1.next
    return merged_list

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


# First Test scenario
# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list.append(Node(second_linked_list))

solution = nested_linked_list.flatten()
expected_list = [1, 2, 3, 4, 5]
flattened_list = []
node = solution.head
while node is not None:
    flattened_list.append(node.value.value)
    node = node.next

print(flattened_list)
print(expected_list)


#testing