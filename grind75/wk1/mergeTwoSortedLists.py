# Definition for singly-linked list.
class ListNode(object):
    """
    A node in a linked list
    Val: the value of this node
    Next: the downstream node 
        (if next is None, then this node can be considered the tail)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    
    def __init__(self):
        self.mergedHead = None
        self.curr = None
    
    def LLToArr(self, list):
        """
        Input - LL
        Output - Arr
        Approach - Keep traversing downstream until next is None
        Time - O(n)
        """
        arr = []
        while list:
            arr.append(list.val)
            list = list.next
        return arr
    
    def appendLL(self, item, curr):
        """
        Input - item, LL node (curr tail)
        Output - LL node (new tail)
        Approach - modify the next value of the current tail, and then update the tail reference
        Time - O(1)
        """
        if curr is None:
            self.mergedHead = ListNode(item)
            self.curr = self.mergedHead
        else:
            curr.next = ListNode(item)
            self.curr = curr.next
    
    def mergeTwoLists(self, list1, list2):
        """
        Input - two sorted LL's
        Output - a merged LL that is sorted
        Approach - Basically copying the logic of the the merge function of mergesort
        Time complexity: O(n), n = combined length of list1 and list2
        """
        arr1 = self.LLToArr(list1)
        arr2 = self.LLToArr(list2)
        
        # l and r are points for list1/list2 respectively
            # this is basically a way of pretending to make actual modifications to the LL
            # that is, every iteration, you pretend to remove the head of the LL that you are appending from
                # now that i think about it, im not sure if the preprocessing LL -> arr is necessary
        l = 0
        r = 0
        
        # look at the head of the two lists and then merge the lowest value
            # keep doing this until one of the lists is empty
            # after that, it will be the case that: 
                # one of the lists will be empty and the other won't
                    # based on the behaviour of choosing the lowest value - 
                    # we can just append the entire remnants of the non-empty list, 
                    # because all those values will be bigger than what's in the current merged list
                    
        while l < len(arr1) and r < len(arr2):
            if arr1[l] < arr2[r]:
                self.appendLL(arr1[l], self.curr)
                l += 1

            else:
                self.appendLL(arr2[r], self.curr)
                r += 1

       
        if r < len(arr2):
            for i in range(r,len(arr2)):
                self.appendLL(arr2[i], self.curr)
                r += 1
        
        if l < len(arr1):
            for i in range(l,len(arr1)):
                self.appendLL(arr1[i], self.curr)
                l += 1
                
        return self.mergedHead
    
sol = Solution()

testList1 = ListNode()
testList1.next = ListNode(1)
testList1.next.next = ListNode(2)
testList1.next.next.next = ListNode(3)

testList2 = ListNode(4)
testList2.next = ListNode(5)
testList2.next.next = ListNode(6)

testList3 = ListNode(0)
testList3.next = ListNode(2)
testList3.next.next = ListNode(6)
testList3.next.next.next = ListNode(8)


testList4 = ListNode(1)
testList4.next = ListNode(3)
testList4.next.next = ListNode(4)
testList4.next.next.next = ListNode(9)

res = sol.mergeTwoLists(testList3, testList4)
print(res)
print(sol.LLToArr(res))
