class Solution:
    # @param A : tuple of integers
    # @return an integer

    def majorityCandidate(self, A):
        maj_index = 0
        count = 1
        for i in range(len(A)):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]

    def isMajority(self,A, cand):
        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > len(A) / 2:
            return True
        else:
            return False
    def majorityElement(self,A):
        majority_candidate=self.majorityCandidate(A)
        is_majority=self.isMajority(A,majority_candidate)
        if is_majority:
            return majority_candidate
        else:
            return -1
if __name__=="__main__":
    A=[2,1,2]
    majority_element=Solution().majorityElement(A)
    print(str(majority_element))