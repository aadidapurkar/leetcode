class Stack():
    def __init__(self):
        self.stack = []
    """
    This is not ideal way to implement stack because insert is O(n) 
    TODO - smarter way - treat the top of the stack like the end of the list instead of the front so you can have O(1) push instead of O(n)
    
    """
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