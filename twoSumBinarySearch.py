

class Solution:
    def binarySearch(self, arr, target):
        #print(arr)
        
        if len(arr) == 1:
            if arr[0][0] == target:
                return arr[0]
            else:
                return None
            
        leftArr = arr[0:len(arr)//2]
        midVal = arr[len(arr)//2][0]
        rightArr = arr[(len(arr)//2)+1:len(arr)]
        
        if target == midVal:
            return (arr[len(arr)//2])

        elif target < midVal:
            return self.binarySearch(leftArr, target)
        
        else:
            return self.binarySearch(rightArr, target)
        
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        
        l = len(arr)
        leftArr = arr[0:l//2]
        rightArr = arr[l-(l//2):l]
        
        leftArr = self.mergeSort(leftArr)
        rightArr = self.mergeSort(rightArr)
        
        return self.merge(leftArr, rightArr)
    
    def merge(self, leftArr, rightArr):
        
        merged = []
        
        while len(leftArr) > 0 and len(rightArr) > 0:
            if leftArr[0][0] > rightArr[0][0]:
                merged.append(rightArr[0])
                rightArr.pop(0)
            else:
                merged.append(leftArr[0])
                leftArr.pop(0)
                
        # only one of these below while loops should execute
        if len(leftArr) > 0:
            merged += leftArr
            
        if len(rightArr) > 0:
            merged += rightArr
        
        return merged
        
    def twoSum(self, nums, target):
        """
        Create a variant of nums with extra info - O(n)
            nstead of elements being numbers, elements are now tuples (number, original index appearance in nums)
        Then, run mergesort on the variant array with the the comparison point / key being the first element in the tuple - O(n * log n)    
        Then,  For each element in the sorted array, run a binary search to try and find the remainder value - O(n * log n) 
            If the binary search found the remainder in the array, then we found a twoSum

        Time complexity: O(n * log n), n = length of nums
        Space complexity: O(n), n = length of nums, auxillary space of storing the sorted arrray
        """
        sol = []
        
        numsWithIndices = []
        for i, num in enumerate(nums):
            numsWithIndices.append((num, i))
            
        sortedNums = self.mergeSort(numsWithIndices)
        #print(sortedNums)
        
        for num in sortedNums:
            res = self.binarySearch(sortedNums, target - num[0])
            #print(res,num)
            if res is not None:
                sol.append(res[1])
                sol.append(num[1])
            
        return list(set(sol))
        
sol = Solution()
print(sol.twoSum([2,7,11,15],9))