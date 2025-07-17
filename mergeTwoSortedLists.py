# Definition for singly-linked list.
class ListNode(object):
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
        Basically copying the logic of the the merge function of mergesort
        Time complexity: O(n), n = combined length of list1 and list2
        """
        arr1 = self.LLToArr(list1)
        arr2 = self.LLToArr(list2)
        print(f"List 1 converted to array: {arr1}")
        print(f"List 2 converted to arr: {arr2}")
        
        l = 0
        r = 0
        
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
