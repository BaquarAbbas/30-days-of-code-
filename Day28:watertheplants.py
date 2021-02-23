'''A gallery with plants is divided into n parts, numbered : 0,1,2,3...n-1.There are provisions for attaching water sprinklers at every partition.
A sprinkler with range x at partition i can water all partitions from i-x to i+x.Given an array gallery[ ] consisting of n integers,
where gallery[i] is the range of sprinkler at partition i (power==-1 indicates no sprinkler attached),
return the minimum number of sprinklers that need to be turned on to water the complete gallery.
If there is no possible way to water the full length using the given sprinklers, print -1.

Example 1:

Input:
n = 6
gallery[ ] = {-1, 2, 2, -1, 0, 0}
Output:
2
Explanation: Sprinklers at index 2 and 5
can water thefull gallery, span of
sprinkler at index 2 = [0,4] and span
â€‹of sprinkler at index 5 = [5,5].
Example 2:

Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
Output:
-1
Explanation: No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.'''
#Solution1
class Solution:
    def min_sprinklers(self, gallery, n):
        sprinklers = [] 
        for i in range(n):
            if gallery[i] > -1:
                sprinklers.append([i-gallery[i],i+gallery[i]]) 
        sprinklers.sort() 
        target = 0 
        sprinklers_on = 0 
        i = 0 
        while target < n:
            if i == len(sprinklers) or sprinklers[i][0] > target:
                return -1 
            max_range = sprinklers[i][1] 
            while i + 1 < len(sprinklers) and sprinklers[i+1][0] <= target:
                i += 1
                max_range = max(max_range,sprinklers[i][1]) 
            if max_range < target:
                return -1 
            sprinklers_on += 1
            target = max_range + 1
            i += 1 
        return sprinklers_on
