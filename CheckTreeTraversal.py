'''Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.'''

#Solution
def checktree(self,preorder, inorder, postorder, N): 
        if N == 0:
            return 1
        
        if N == 1:
            return preorder[0] == inorder[0] and inorder[0] == postorder[0]
            
        idx = -1 
        
        for i in range(n):
            if inorder[i] == preorder[0]:
                idx = i 
                break 
        
        if idx == -1:
            return 0 
        
        return self.checktree(preorder[1:],inorder,postorder,idx) and self.checktree(preorder[idx+1:],inorder[idx+1:],postorder[idx:],N - idx -1) 
