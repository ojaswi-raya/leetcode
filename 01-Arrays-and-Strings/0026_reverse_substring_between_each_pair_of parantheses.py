class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop until matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # Pop the opening '('
                stack.pop()
                
                # Push reversed characters back to stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)