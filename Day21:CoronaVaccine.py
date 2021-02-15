'''Geek has developed an effective vaccine for Corona virus and he wants each of the N houses in Geek Land to have access to it.
Given a binary tree where each node represents a house in Geek Land,find the minimum number of houses that should be supplied with the vaccine kit
if one vaccine kit is sufficient for that house,its parent house and it's immediate child nodes.  
Example 1:
Input:
    1
   / \
  2   3 
        \
         4
          \
           5
            \
             6
Output:
2
Explanation:
The vaccine kits should be 
supplied to house numbers 1 and 5. 
Example 2:

Input:
    1
   / \
  2   3 
Output:
1
Explanation:
The vaccine kits should be 
supplied to house number 1.'''
#Solution
class Solution:
    def supplyVaccine(self, root):
        vaccinekit,dist = self.traverse(root) 
        if dist == 3:
            return vaccinekit + 1
        return vaccinekit 
    
    def traverse(self,n):
        if not n:
            return (0,2) 
        vaccinekitl,distl = self.traverse(n.left) 
        vaccinekitr,distr = self.traverse(n.right) 
        
        if max(distl,distr) == 3:
            return (vaccinekitl+vaccinekitr+1,1)
                
        return (vaccinekitl + vaccinekitr,1+min(distl,distr))
