class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def get_length(self,A):
        temp=A
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count

    def solve(self, A):
        length_of_ll=self.get_length(A)
        if length_of_ll==1:
            return None
        temp=A
        if length_of_ll%2 == 0:
            k=int(length_of_ll/2)
        else:
            k = int(length_of_ll / 2)
        count=0
        while count<k-1:
            temp = temp.next
            count = count + 1
        temp.next=temp.next.next
        return A

if __name__=='__main__':
    head=ListNode(1)
    temp=head
    temp.next=ListNode(2)
    temp=temp.next
    temp.next=ListNode(3)
    temp=temp.next
    temp.next=ListNode(4)
    temp=temp.next
    temp.next=ListNode(5)
    temp = temp.next
    temp.next = ListNode(6)
    temp=Solution().solve(head)
    head=temp
    while temp!=None:
        print(str(temp.val))
        temp=temp.next


