class Node:
    def init(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def init(self):
        self.head = None
        self.length = 0


ll = LinkedList()

def insert_node(self, position, value):
    # @param position, an integer
    # @param value, an integer
    if position > ll.length + 1:
        return
    newNode = Node(value)
    c = 0
    temp = ll.head
    if position == 1:
        newNode.next = ll.head
        ll.head = newNode
        ll.length += 1
    else:
        c = 1
        while c < position - 1:
            temp = temp.next
            c += 1
        newNode.next = temp.next
        temp.next = newNode
        ll.length += 1


def delete_node(position):
    # @param position, integer
    # @return an integer
    if position > ll.length:
        return
    temp = ll.head
    if position == 1:
        newhead = temp.next
        ll.head = newhead
        ll.length -= 1
    else:
        c = 1
        while c < position - 1:
            temp = temp.next
            c += 1
        newval = temp.next.next
        temp.next = newval
        ll.length -= 1


def print_ll():
    # Output each element followed by a space
    temp = ll.head
    while temp.next:
        print(temp.data)
        temp = temp.next
    if (temp):
        print(temp.data)
    print()




