class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n=len(A)
        if n==0:
            return "No"
        else:
            final_num=A[0]
            for i in range(1,n):
                final_num=final_num^A[i]
            if final_num&1==0:
                return "Yes"
            else:
                return "No"

if __name__=='__main__':
    A=[9,17]
    is_interesting=Solution().solve(A)
    print(is_interesting)