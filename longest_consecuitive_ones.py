class Solution:
    # @param A : string
    # @return an integer
    def count_of_ones(self, A):
        count = 0
        for char in A:
            if char == "1":
                count = count + 1
        return count

    def find_max(self, x, y):
        if x > y:
            return x
        return y

    def solve(self, A):
        max_length = 0
        total_count = self.count_of_ones(A)
        #print("Total number:" + str(total_count))
        for i, char in enumerate(A):

            rc = 0
            lc = 0
            if char == "0":
                for j in range(i-1,-1,-1):
                    if A[j] == "1":
                        lc = lc + 1
                    else:
                        break
                for k in range(i + 1, len(A)):
                    if A[k] == "1":
                        rc = rc + 1
                    else:
                        break
                count_temp=lc+rc
                #print("Temp count:" + str(count_temp)+" for index:"+str(i))
                if count_temp < total_count:
                    count_temp = count_temp+1

                max_length = self.find_max(max_length, count_temp)

        if max_length==0:
            max_length=total_count
        return max_length


if __name__ == "__main__":
    A = "010100110101"
    length = Solution().solve(A)
    print(str(length))
