class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Build dictionary for O(1) lookups
        know_dict = {key: val for key, val in knowledge}
        
        res = []
        key_buf = []
        in_bracket = False
        
        # Step 2: Parse string
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(key_buf)
                res.append(know_dict.get(key, "?"))
                key_buf.clear()
            elif in_bracket:
                key_buf.append(char)
            else:
                res.append(char)
                
        return "".join(res)