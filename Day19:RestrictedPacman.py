'''In the game of Restricted Pacman, an infinite linear path is given.
Pacman has to start at position 0 and eat as many candies as possible.
In one move he can only jump a distance of either M or N.If M and N are coprime numbers,
find how many candies will be left on the board after the game is over.
Note: The result is always finite as after a point X every index in the infinite path can be visited. 
Example 1:
Input: M = 2, N = 5
Output: 2
Explanation: From index 0, the indices that 
can be visited are
0 + 2 = 2
0 + 2 + 2 = 4
0 + 5 = 5
0 + 2 + 2 + 2 = 6
0 + 2 + 5 = 7
0 + 2 + 2 + 2 + 2 = 8
0 + 2 + 2 + 5 = 9
0 + 5 + 5 = 10
and so on.
1 and 3 are the only indices that cannot be 
visited. Therefore the candies at these two 
positions will be left on the board. 
'''
#Solution1
class Solution:
    def restrictedPacman(self,m,n):
        max_num = m*n - m -n 
        lis = [max_num] 
        num_set = {max_num}
        while lis:
            curr = lis[0] 
            lis.remove(lis[0]) 
            
            if curr - m > 0 and curr-m not in num_set:
                num_set.add(curr-m)
                lis.append(curr-m)
            if curr - n > 0 and curr-n not in num_set:
                num_set.add(curr-m)
                lis.append(curr-m)
        return len(num_set) 
#Solution2
class Solution: 
    def candies(self,m,n): 
        res = m*n -(m+n) 
        return res//2 + 1
