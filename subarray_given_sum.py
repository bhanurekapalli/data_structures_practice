class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n=len(A)
        left=0
        right=0
        sub_sum=A[right]
        while(left<=right and right<n):
            if left==right:
                sub_sum=A[right]
            if sub_sum==B:
                final_list=A[left:right+1]
                return final_list
            elif sub_sum<B:
                right=right+1
                if right<n:
                    sub_sum = sub_sum + A[right]
            else:
                if sub_sum>B:
                    sub_sum=sub_sum-A[left]
                    left = left + 1
                    if left > right and left <n:
                        right=left
        return [-1]

if __name__=='__main__':
    A=[ 15, 2, 5, 6, 9 ]
    B=7
    answer=Solution().solve(A,B)
    print(answer)
