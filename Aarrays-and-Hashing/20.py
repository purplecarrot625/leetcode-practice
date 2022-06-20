class Solution:
    def isValid(self, s: str) -> bool:
        closeParenthesesMap = {")":"(", "}":"{", "]": "["}
        stack = []
        
        for c in s:
            if c in closeParenthesesMap:
                if stack and stack[-1] == closeParenthesesMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        
        
# we need a stack
# we need a map: close->open
# traverse the string
# edge case: stack is empty
# if the current character is a close parentheses(c in map): pop the top element, and if they are the same, continue, if not, return false

#return true if the stack is empty