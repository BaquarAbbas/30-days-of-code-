'''Cupid wants to strike maximum houses in Geek Land on Valentine's Day.
The houses in Geek Land are arranged in the form of a binary tree. Cupid is standing at target node initially. 
Find the sum of all nodes within a maximum distance k from target node.The target node should be included in the sum.
Example 1:

Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
target = 9, K = 1
Output:
22
Explanation:
Nodes within distance 1 from 9 are 9, 5, 7, 1  
Example 2:

Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
target = 40, K = 2
Output:
113
Explanation:
Nodes within distance 2 from 40 are 40, 19, 50, 4
'''
#Solution1
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def add_subtree(self, n, dist):
        if n is None or dist<0:
            return 0
        return n.data + self.add_subtree(n.left,dist-1) + self.add_subtree(n.right,dist-1)
    
    def traverse(self, n ,target, k):
        if n is None:
            return (0,-1)
        if n.data==target:
            return (self.add_subtree(n,k), k-1)
            # adding all nodes within range in the sub tree below
            # and returning sum
        
        Sum,dist = self.traverse(n.left, target, k)
        if Sum>0:
            # Sum>0 indicates target was found in left subtree
            if dist==-1:
                return (Sum,dist)
            return ( Sum+n.data + self.add_subtree(n.right,dist-1) , dist-1 )
            # adding values from right sub tree
        
        Sum,dist = self.traverse(n.right, target, k)
        if Sum>0:
            # Sum>0 indicates target was found in right subtree
            if dist==-1:
                return (Sum,dist)
            return ( Sum+n.data + self.add_subtree(n.left,dist-1) , dist-1 )
            # adding values from left sub tree
        
        return (0,-1)
    
    def sum_at_distK(self, root, target, k):
        Sum,dist = self.traverse(root, target, k)
        return Sum
