'''There are N buildings in Linear Land.
They appear in a linear line one after the other and their heights are given in the array arr[].
Geek wants to select three buildings in Linear Land and remodel them as recreational spots.
The third of the selected building must be taller than the first and shorter than the second.
Can geek build the three-building recreational zone?
Example 1:
  Input: N = 6, arr[] = {4, 7, 11, 5, 13, 2}
  Output: True
  Explanation: [4, 7, 5] fits the condition.'''

#Solution 
class Solution:
    def recreationalSpot(self,arr,n):
        fi = float('inf') 
        for i in range(n):
            fi = min(fi,arr[i])
            if i != n-1:
                if arr[i+1] < arr[i] and arr[i] > fi:
                    return True 
        return False 
