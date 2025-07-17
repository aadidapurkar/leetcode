class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.insert(0,item)
        
    def pop(self):
        return self.stack.pop(0)
    
    def peek(self):
        return self.stack[0]
        
        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        opening = ["(","[","{"]
        closing = [")","]","}"]
        closingOpening = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char in opening:
                stack.push(char)
                
            if char in closing:
                peeked = stack.peek()
                if closingOpening[char] == peeked:
                    stack.pop()
                else:
                    return False
        return True

sol = Solution()
print(sol.isValid("([])"))