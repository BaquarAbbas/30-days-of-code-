''''''

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
