class Solution:
    def twoSum(self, nums, target):
        """
        Sort nums with a sorting algorithm -> O(n * log n)

        Iterate through nums to find remainder required at each index, O(n)
            And in each iteration, run a binary search on sorted nums to look for remainder O(log n)

        Time complexity: O(n * log n), n = length of nums
        Space complexity: O(n), n = length of nums, auxillary space of storing the sorted arrray
        """
        sortedNums = mergeSort(nums)
        for i, num in nums:


sol = Solution()
print(sol.twoSum([3,2,4],6))
