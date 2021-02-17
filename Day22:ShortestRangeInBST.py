'''Given a BST (Binary Search Tree), find the shortest range [x, y],
such that, at least one node of every level of the BST lies in the range.
If there are multiple ranges with the same gap (i.e. (y-x))
return the range with the smallest x.
Example 1:
Input:
              8
          /   \
         3     10
       /  \      \
      2    6      14
          / \     /
         4   7   12
                /  \
               11   13
Output: 6 11
Explanation: Level order traversal of the tree 
is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13]. 
The shortest range which satisfies the above 
mentioned condition is [6, 11]. 

Example 2:

Input:
   12
    \
     13
       \
        14
         \
          15
           \
           16

Output: 12 16
Explanation: Each level contains one node, 
so the shortest range is [12, 16].'''
#Solution1 
class Solution:
    def shortestRange(self, root):
        def storein(root, lvl, lin, llv):
            if not root:
                return
            storein(root.left,lvl+1,lin,llv)
            lin.append(root.data)
            llv.append(lvl)
            storein(root.right,lvl+1,lin,llv)
    
    
        inorder=[]
        level=[]
        storein(root,0,inorder,level)
        
        i=j=k=cntzero=0
        maxDepth=max(level)+1
        depth=[0]*maxDepth
        for k in range(len(level)):
            depth[level[k]]+=1
            if level[k]==0:
                j=k
                break
        
        cntzero=depth.count(0)
        x,y=inorder[0],inorder[-1]
        if cntzero==0:
            x,y=inorder[i],inorder[j]
    
        while i<=k and j<len(inorder):
            while j<len(inorder):
                if cntzero==0:
                    if (y-x) > (inorder[j]-inorder[i]):
                        x,y=inorder[i],inorder[j]
                    break
                j+=1
    
                if j>= len(inorder):
                    break
                if depth[level[j]]==0:
                    cntzero-=1
                depth[level[j]]+=1
            
            while not cntzero and i<=k:
                if (y-x)>(inorder[j]-inorder[i]):
                    x,y=inorder[i],inorder[j]
                depth[level[i]]-=1
                if depth[level[i]]==0:
                    cntzero+=1
                i+=1
        
        return (x,y)
