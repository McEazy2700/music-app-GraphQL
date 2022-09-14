class Node:
    def __init__(self, value:int, next:object=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"<Node value={self.value}>"

class LinkedList:
    def __init__(self, head:Node):
        self.head = head


