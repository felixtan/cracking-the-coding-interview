class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'<singly_linked.Node {self.value}>'

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    # O(1)
    def append(self, value):
        temp = Node(value)
        self.tail.next = temp
        self.tail = temp

    # O(1)
    def prepend(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    # O(n)
    # delete the first node with value
    def delete(self, value):
        node = self.head
        
        if node.value == value:
            self.head = node.next
            return self.head

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                if node.next is None:
                    self.tail = node
                return self.head
            else:
                node = node.next

        return self.head


    def __repr__(self):
        node = self.head
        values = [node.__repr__()]
        while node.next:
            node = node.next
            values.append(node.__repr__())
        return f"[{', '.join(values)}]"