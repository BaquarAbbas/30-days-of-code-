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
    def digitSum(self,num):
        ans = 0 
        for i in str(num):
            ans += int(i)
        return ans  
    def RulingPair(self,arr,n):
        ans = -1
        dic = dict() 
        for i in arr:
            sm = self.digitSum(i) 
            if sm in dic:
                ans = max(ans,i+dic[sm])
                dic[sm] = max(dic[sm],i)
            else:
                dic[sm] = i 
        return ans 
