class Node:
    data = 0
    next = None

    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    head = None
    size = 0

    def solve(self, A):
        for array in A:
            type, value, index = array

            # add node(value) before first element
            if type == 0:
                n = Node(value)
                n.next = self.head
                self.head = n
                self.size += 1

            # Add node(value) at the last 
            elif type == 1:
                n = Node(value)
                if self.size == 0:
                    n.next = self.head
                    self.head = n
                else:
                    temp = self.head
                    for i in range(self.size - 1):
                        temp = temp.next
                    temp.next = n
                self.size += 1

            # add node(value) before index
            elif type == 2:
                if index > self.size:
                    # bad index
                    continue

                n = Node(value)
                if index == 0:
                    n.next = self.head
                    self.head = n
                else:
                    temp = self.head
                    for i in range(index - 1):
                        temp = temp.next
                    n.next = temp.next
                    temp.next = n
                self.size += 1

            # delete
            elif type == 3:

                del_index = value  # 2nd postion is the index in delete
                if del_index > self.size:
                    continue
                if del_index == 0:
                    self.head = self.head.next
                else:
                    temp = self.head
                    for i in range(del_index - 1):
                        temp = temp.next
                    temp.next = temp.next.next
                self.size -= 1

        return self.head


if __name__ == "__main__":
    A = [
        [0, 1, -1],
        [1, 2, -1],
        [2, 3, 1]
    ]
    root = Solution().solve(A)
