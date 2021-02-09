'''Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. 
Count distinct triplets in the list that sum up to given integer X.
Example 1:
Input: LinkedList: 1->2->4->5->6->8->9, X = 17
Output: 2
Explanation: Distinct triplets are (2, 6, 9) 
and (4, 5, 8) which have sum equal to X i.e 17.
'''
#Solution1 
def countTriplets(head,x):
    # code here
    ptr2 = head 
    count = 0 
    um = dict() 
    ptr = head 
    while ptr != None:
        um[ptr.val] = ptr 
        ptr = ptr.nxt 
        
    ptr1 = head 
    while ptr1 != None:
        ptr2 = ptr1.nxt 
        while ptr2 != None:
            p_sum = ptr1.val + ptr2.val 
            
            if ((x-p_sum) in um) and um[x - p_sum] != ptr1 and um[x - p_sum] != ptr2:
                count += 1 
            ptr2 = ptr2.nxt 
        ptr1 = ptr1.nxt 
        
    return count // 3 
