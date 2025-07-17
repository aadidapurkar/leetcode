class Solution(object):
    def preprocess(self, s):
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    def isPalindrome(self, s):
        """
        Approach: Preprocess the string, divide  the string in two halves, and compare the halves from opposite ends, char by char
        Time O(n) - n = length(s), best case would be when there's an early mismatch, worst case would be when the string is a palindrome
        """
        string = self.preprocess(s)

        """
        Split halves based on two cases
        If the length of the string is even, then you're splitting the half right down the middle
        If hte length is odd, then we 'pretend' the string is even by considering the median as redundant because it will always symettrically support the palindrome
        So basically we're converting an odd case -> even case
        """
        if len(string) % 2 == 0:
            leftSide = string[0:len(string)//2]
            rightSide = string[len(string)//2:len(string)]
        else:
            leftSide = string[0:len(string)//2]
            rightSide = string[(len(string)//2)+1:len(string)]

        size = len(leftSide) # or len(rightSide) - doesn't make a difference
        leftI = 0
        rightI = size - 1
        
        for _ in range(size):
            if leftSide[leftI] != rightSide[rightI]:
                return False
            leftI += 1
            rightI -= 1
        return True
        
sol = Solution()
print(sol.isPalindrome("aba"))