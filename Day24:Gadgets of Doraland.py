'''In Doraland, people have unique Identity Numbers called D-id.
Doraemon owns the most popular gadget shop in Doraland.
Since his gadgets are in high demand and he has only K gadgets left
he has decided to sell his gadgets to his most frequent customers only.
N customers visit his shop and D-id of each customer is given in an array array[ ].
In case two or more people have visited his shop the same number of time he gives priority to the
customer with higher D-id. Find the D-ids of people he sells his K gadgets to.

Example 1:
Input: N = 6, array[] = {1, 1, 1, 2, 2, 3}, K = 2
Output: 1 2
Explanation: Customers with D-id 1 and 2 are most frequent.

Example 2:
Input: N = 8, array[] = {1, 1, 2, 2, 3, 3, 3, 4}, K = 2
Output: 3 2
Explanation: People with D-id 1 and 2 have visited shop 2 times Therefore, in this case, the answer includes the D-id 2 as 2 > 1.
'''
#Solution
import operator 
class Solution:
    def Topk(self,array,k):
        dt = {} 
        for x in array:
            dt[x] = dt.get(x,0)+1 
        dt1 = {} 
        for x in dt.keys():
            if dt[x] not in dt1:
                dt1[dt[x]] = [] 
            dt1[dt[x]].append(x) 
        arr = sorted(list(dt1.items()),key =operator.itemgetter(0),reverse = True)
        ans = [] 
        count = 0
        for x in arr:
            x[1].sort(reverse = True)
            for item in x[1]:
                if count == k:
                    return ans 
                ans.append(item)
                count += 1
        return ans
