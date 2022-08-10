class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        final_list=[0]*A
        for row in B:
            L=row[0]-1
            R=row[1]-1
            amount=row[2]
            final_list[L]=final_list[L]+amount
            if R<A-1:
                final_list[R+1]=final_list[R+1]-amount
        initial_sum=0
        for i in range(0,A):
            initial_sum = initial_sum + final_list[i]
            final_list[i]=initial_sum
        return final_list

if __name__=='__main__':
    A=5
    B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    print(Solution().solve(A,B))