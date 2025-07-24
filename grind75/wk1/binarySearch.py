from typing import List

class Solution:
    def search(self, nums: List[int], target: int,l=None,r=None) -> int:
        if l is None and r is None:
            l = 0
            r = len(nums)

        if l == r:
            if nums[l] != target:
                return -1
            else:
                return l
            
        mid = (r-l) // 2 + l
        midVal = nums[mid]

        if target == midVal:
            return mid
        
        elif target < midVal:
            return self.search(nums, target, l, mid-1)
        
        elif target > midVal:
            return self.search(nums, target, mid+1, r)

sol = Solution()
sol.search([-1,0,3,5,9,12],9)