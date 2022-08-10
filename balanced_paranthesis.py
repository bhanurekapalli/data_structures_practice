class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data


class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        a_stack = Stack()
        n = len(A)
        i = 0
        while i < n:
            if A[i] == '(':
                a_stack.push('(')
                i = i + 1
            else:
                top_element = a_stack.pop()
                if top_element == '(':
                    i = i + 1
                    continue
                else:
                    return 0
        top_element=a_stack.pop()
        if top_element is None:
            return 1
        else:
            return 0

if __name__ == '__main__':
    A = '(()())'
    is_balanced = Solution().solve(A)
    print(str(is_balanced))
