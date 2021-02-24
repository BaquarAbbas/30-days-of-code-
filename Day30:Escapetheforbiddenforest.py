'''Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them.
But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety.
The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. 
Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges 
that Penelope can build and save everyone from the Devil. 
Note: Each tree in the forest belongs to one of the 3 categories represented by * or # or @

Example 1:

Input:
str1 = "*@#*" 
str2 = "*#"
Output:
2
Explanation:
str1 = "*@#*" and str2 = "*#" 
Two bridges can be built between the banks 
of the river in the following manner. 
* @ # *
|      |
*     #
Example 2:

Input:
str1 = "***"
str2 = "##"
Output:
0'''
#Solution1
class Solution:
    def build_bridges(self, str1, str2):
        m = len(str1)
        n = len(str2)
        lcs = [[None]*(n+1) for i in range(m+1)] 
        
        for i in range(m+1):
            for j in range(n+1):
                if i ==0 or j == 0:
                    lcs[i][j] = 0 
                elif str1[i-1] == str2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1 
                else:
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
        return lcs[m][n]
