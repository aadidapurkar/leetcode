class Solution:
    def isAnagram(self, s1, s2) -> bool:
    # Approach - Create a frequency table for one of the strings,
    # and then parse the other string, the strings are anagrams iff
    # it never needs to borrow a frequency @ zero
    # Time - O(s + t)

        frequencyS1 = {}
        
        for char in s1:
            if char in frequencyS1:
                frequencyS1[char] += 1
            else:
                frequencyS1[char] = 1
        
        print(frequencyS1)

        for char in s2:
            if char in frequencyS1:
                curr = frequencyS1[char]
            else:
                return False
            if curr == 0:
                return False
            else:
                frequencyS1[char] -= 1
        return True
    
sol = Solution()
print(sol.isAnagram("rat","car"))