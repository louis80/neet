class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False 

        dic_matching = {
            '(': ')', 
            '[': ']', 
            '{': '}'
        } 

        stack = []

        for char in s:
            if char in dic_matching:
                stack.append(char)
            elif not len(stack):
                return False
            elif dic_matching[stack.pop()] != char:
                return False

        if len(stack):
            return False
                
        return True 