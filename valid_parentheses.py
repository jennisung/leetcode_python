class Solution:
    def isValid(self, s: str) -> bool:
        # Algorithm:
        # 1- Initialize an empty stack. 
        # 2- For each character in the string, If it's an opening parenthesis, push it onto the stack. If it's a closing parenthesis, check if the stack is empty or if the top of the stack matches the corresponding opening parenthesis. 
        #    If not, return False.
        # 3- After going through all characters, check if the stack is empty.
        #    If it is, return True. If not, return False.
        # 4-The result is True if all parentheses are correctly matched, otherwise False.
        
        # Big - O: Time and space : O(n) 


        stack = []
        
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack



