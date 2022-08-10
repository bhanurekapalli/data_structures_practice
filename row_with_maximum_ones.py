class Solution:
    def find_max(self,x,y):
        if x>y:
            return x
        return y
    def get_first_1_index(self,row):
        n=len(row)
        for i in range(0,n):
            if row[i]==1:
                return i
        return -1

    def solve(self, A):
        max_ones = -10
        row_num = -1

        for i,row in enumerate(A):
            first_one_index=Solution().get_first_1_index(row)
            n = len(row)
            if first_one_index!=-1:
                num_of_ones=n-first_one_index+1
                if max_ones!=num_of_ones:
                    max_ones=Solution().find_max(max_ones,num_of_ones)
                    if num_of_ones==max_ones:
                        row_num=i
        return row_num

if __name__ == '__main__':
    A = [[0,0],[0,1]]
    print(str(Solution().solve(A)))
