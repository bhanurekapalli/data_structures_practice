class Solution:
    def trap(self, A):
        n = len(A)
        if n<3:
            return 0
        total_trapped = 0
        max_left=0
        max_right=0
        left=0
        right=n-1
        while left<=right:
            if A[left]<=A[right]:
                if A[left]>=max_left:
                    max_left=A[left]
                else:
                    total_trapped=total_trapped+(max_left-A[left])
                left=left+1
            else:
                if A[right]>=max_right:
                    max_right=A[right]
                else:
                    total_trapped=total_trapped+(max_right-A[right])
                right=right-1
        return total_trapped


if __name__ == '__main__':
    A = [2,1,3]
    print(str(Solution().trap(A)))
