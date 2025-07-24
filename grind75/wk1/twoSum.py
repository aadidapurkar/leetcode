class Solution:
    def twoSum(self, nums, target):
        """
        Compare each pair of indices
        If they are not the same index, and they add to target, that's the answer

        Time complexity: O(n^2), n = length of nums
        Space complexity: O(1), no auxillary space required
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and i != j:
                    print(num1, num2, i, j)
                    return [i,j]

sol = Solution()
print(sol.twoSum([3,2,4],6))
