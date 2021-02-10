'''Given a string S and an integer K, the task is to reduce the string by applying the following operation:
Choose a group of K consecutive identical characters and remove them. 
The operation can be performed any number of times until it is no longer possible.
Example1
Input:
K = 2
S = "geeksforgeeks"
Output:
gksforgks
Explanation:
Modified String after each step: 
"geegsforgeeks" -> "gksforgks"
'''
#Solution1
class Solution:
    def Reduced_String(self, k, s):
        count = [] 
        stack = "" 
        emp = ''
        if k == 1:
            return emp 
        for i in range(len(s)):
            if i == 0 or not stack or s[i]  != stack[-1]:
                count.append(1) 
                stack += s[i]
            else:
                recount = count.pop() + 1 
                if recount == k:
                    stack = stack[:len(stack)-1]
                    
                else:
                    count .append(recount)
        return "".join(map(lambda x,y:x*y,count,stack))
    
#Solution2
class Solution:
    def Reduced_String(self, k, s):
        stack = [] 
        emp = ''
        if k == 1:
            return emp  
        for i in range(len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1 
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i],1])
                
        out = '' 
        while stack:
            char,freq = stack.pop() 
            out += (char * freq) 
            
        return out[::-1]

