class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head is None:
            return None
        popped=self.head.data
        self.head=self.head.next
        return popped

    def peek(self):
        if self.head is None:
            return -1
        else:
            return self.head.data

class MinStack:
    # @param x, an integer
    def __init__(self):
        self.main_stack=Stack()
        self.min_stack=Stack()
        self.min=None
    def push(self, x):
        self.main_stack.push(x)
        if self.min is None:
            self.min=x
            self.min_stack.push(self.min)
        else:
            if x <= self.min:
                self.min=x
                self.min_stack.push(self.min)

    # @return nothing
    def pop(self):
        popped=self.main_stack.pop()
        x=self.min_stack.peek()
        if not popped is None:
            if popped == x:
                self.min_stack.pop()
                if self.min_stack.peek()==-1:
                    self.min=None
                else:
                    self.min=self.min_stack.peek()

    # @return an integer
    def top(self):
        top_element=self.main_stack.peek()
        return top_element

    # @return an integer
    def getMin(self):
        top_min=self.min_stack.peek()
        return top_min

if __name__=='__main__':
    min_s=MinStack()
    #min_s.push(1)
    #min_s.push(2)
    #min_s.push(-2)
    print(str(min_s.getMin()))
    min_s.pop()
    #print(str(min_s.getMin()))
    print(str(min_s.top()))


