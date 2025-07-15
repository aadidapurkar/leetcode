from typing import List


class Solution:

    def mergeSort(self, arr):
        l = len(arr)
        if l == 1:
            return
        
        mid = l // 2
        leftArr = arr[0:mid]
        rightArr = arr[mid:l]

        self.mergeSort(leftArr)
        self.mergeSort(rightArr)
        self.merge(leftArr, rightArr, arr)

    def merge(self, leftArr, rightArr, arr):
        leftL = len(leftArr)
        rightL = len(rightArr)
        i = 0
        l = 0
        r = 0
        while l < leftL and r < rightL:
            if leftArr[l] < rightArr[r]:
                arr[i] = leftArr[l]
                i += 1
                l += 1
            else:
                arr[i] = rightArr[r]
                i += 1
                r += 1
        
        while l < leftL:
            arr[i] = leftArr[l]
            i += 1
            l += 1
        
        while r < rightL:
            arr[i] = rightArr[r]
            i += 1
            r += 1


    def twoSum(self, nums: List[int], target: List[int]):
        """
        Sort nums with a sorting algorithm -> O(n * log n)

        Iterate through nums to find remainder required at each index, O(n)
            And in each iteration, run a binary search on sorted nums to look for remainder O(log n)

        Time complexity: O(n * log n), n = length of nums
        Space complexity: O(n), n = length of nums, auxillary space of storing the sorted arrray
        """

sol = Solution()
print(sol.mergeSort([8,2,5,3,4,7,6,1]))
