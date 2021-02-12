'''Professor X wants his students to help each other in the chemistry lab. 
He suggests that every student should help out a classmate who scored less marks than him in chemistry and 
whose roll number appears after him. But the students are lazy and they don't want to search too far. 
They each pick the first roll number after them that fits the criteria.
Find the marks of the classmate that each student picks.
Note: one student may be selected by multiple classmates.
Example 1:
Input: N = 5, arr[] = {3, 8, 5, 2, 25}
Output: 2 5 2 -1 -1
Explanation: 
1. Roll number 1 has 3 marks. The first person 
who has less marks than him is roll number 4, 
who has 2 marks.
2. Roll number 2 has 8 marks, he helps student 
with 5 marks.
3. Roll number 3 has 5 marks, he helps student 
with 2 marks.
4. Roll number 4 and 5 can not pick anyone as 
no student with higher roll number has lesser 
marks than them. This is denoted by -1.
Output shows the marks of the weaker student that 
each roll number helps in order. ie- 2,5,2,-1,-1'''

#Solution1
class Solution:
    def help_classmate(self, arr, n):
        res = [-1 for _ in range(n)] 
        for i in range(n-1):
            for j in range(i + 1,n):
                if arr[i] > arr[j]:
                    res[i] = arr[j]
                    break
        return res 
   
#Solution2 
class Solution:
    def help_classmate(self, arr, n):
        stack =[] 
        ans = [] 
        for x in arr[::-1]:
            while stack and stack[-1] >= x:
                stack.pop()
            if stack:
                ans.append(stack[-1]) 
            else:
                ans.append(-1) 
            stack.append(x) 
            
        return ans[::-1]
