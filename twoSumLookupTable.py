class Solution:
    def twoSum(self, nums, target):
        """
        Iterate through nums and create a dictionary knownIndices
            Keys represent numbers, values represent the indices which the number occurs at
            O(n), n = length of nums

        Iterate through nums once again
            Consider the current number i being iterated on
            And that to find a twoSum, we need another number in nums that is exactly target - i
            And we can find that remainder number in O(m) time, 
            Where m = # occurences of remainder in nums, which is usually just 1
            So instead of looking for remainder in O(n) time, we're finding it in O(m)
        
        Time complexity: O(n*m), n = length nums, m = num in nums with most amount of occurences/duplicate appearances
        Space complexity: O(n), auxillary space needed for lookup table size *up to* nums if there are no duplicates
        """
        knownIndices = {}
        for i, num in enumerate(nums):
            if num in knownIndices:
                knownIndices[num].append(i)
            else:
                knownIndices[num] = [i]
        print(knownIndices)

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in knownIndices:
                for index in knownIndices[remainder]:
                    if index != i:
                        return [i,index]

sol = Solution()
print(sol.twoSum([3,2,4],6))
