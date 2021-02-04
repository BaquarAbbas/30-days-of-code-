'''Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. 
If B cannot be a substring of A no matter how many times it is repeated, return -1.

Input: A = "abcd", B = "cdabcdab"
Output: 3
Explanation: After repeating A three times, 
we get "abcdabcdabcd".
'''
#Solution1 
def repeatedStringMatch(self, A, B):
        res = 1
        for i in range(min(len(A),len(B))):
            if B in A:
                return res
            else:
                A += A 
                res += 1
        return -1 
        
#Solution2 
def repeatedStringMatch(self, A, B):
        m = len(A)
        n = len(B)
        for i in range(m):
            if A[i] == B[0]:
                k = i 
                count = 1 
                for j in range(n):
                    if k >= len(A):
                        k = 0 
                        count = count + 1
                    if A[k] != B[j]:
                        break 
                    k = k + 1
                else:
                    return count
                
        return -1
        


