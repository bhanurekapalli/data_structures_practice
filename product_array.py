class Solution:
    # @param A : list of integers
    # @return a list of integers
    def get_product(self,A):
        n=len(A)
        product=1
        for i in range(0,n):
            x=A[i]
            product=product*x
        return product
    def solve(self, A):
        n=len(A)
        total_product=self.get_product(A)
        B=[0]*n
        for i in range(0,n):
            x=int(A[i])
            y=int(total_product/x)
            B[i]=y
        return B

if __name__ == '__main__':
    A = [1,2,3]
    product_array = Solution().solve(A)
    print(product_array)