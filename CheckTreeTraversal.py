'''Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.'''

#Solution
class Solution:
    def checktree(self,preorder,inorder,postorder,n):
        if not n:
            return True 
        if n == 1:
            return preorder[0] == postorder[0] and postorder[0] == inorder[0]
            
        idx = -1
        for i in range(n):
            if inorder[i] == preorder[0]:
                idx = i 
                break 
        if idx  == -1:
            return 0 
        
        if preorder[0] != postorder[n-1]:
            return 0 
            
        left = self.checktree(preorder[1:],inorder,postorder,idx) 
        right = self.checktree(preorder[idx+1:],inorder[idx+1:],postorder[idx:],n - idx -1) 
        
        return left and right  
'''preorder = [1,2,4,5,3]
inorder = [4,2,5,1,3] 
postorder = [4,5,2,3,1] 
n = 5
print(Solution().checktree(preorder,inorder,postorder,n)) '''
