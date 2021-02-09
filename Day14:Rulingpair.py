'''Geek Land has a population of N people and each person's ability to rule the town is measured by a numeric value arr[i]. 
The two people that can together rule Geek Land must be compatible with each other i.e.,
the sum of digits of their ability arr[i] must be equal. Their combined ability should be maximum amongst all the possible pairs of people.
Find the combined ability of the Ruling Pair.

Example 1:
  Input: N = 5, arr[] = {55, 23, 32, 46, 88}
  Output: 101
  Explanation: All possible pairs that are compatible with each other are- (23, 32) with digit sum 5 and (55, 46) with digit sum 10.
  Out of these the maximum combined ability pair is (55, 46) i.e. 55 + 46 = 101'''



class Solution:    
    def RulingPair(self, arr, n): 
    	# Your code goes here
        def findSum(x):
                temp = 0
                while x > 0:
                        temp += x%10
                        x = x//10
                return temp
                
        
        dt = {}
        ans = -1
        arr.sort()
        for x in arr:
                digitsum = findSum(x)
            
                if digitsum in dt:
                        ans = max(ans,x+dt[digitsum][-1])
                else:
                        dt[digitsum] = []
                dt[digitsum].append(x)
        return ans
