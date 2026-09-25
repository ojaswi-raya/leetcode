import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str) -> set[str]:
            if not expr:
                return {""}
            
            # Find top-level commas to split union groups
            groups = []
            start = 0
            brace_count = 0
            
            for i, char in enumerate(expr):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                elif char == ',' and brace_count == 0:
                    groups.append(expr[start:i])
                    start = i + 1
            groups.append(expr[start:])
            
            # If top-level commas exist, return union of all group evaluations
            if len(groups) > 1:
                res = set()
                for group in groups:
                    res |= parse(group)
                return res
            
            # No top-level commas: evaluate concatenated factors
            # Identify first factor (single letter or {...})
            if expr[0] != '{':
                i = 0
                while i < len(expr) and expr[i].isalpha():
                    i += 1
                first_set = {expr[:i]}
                rest_expr = expr[i:]
            else:
                brace_count = 0
                for i, char in enumerate(expr):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            # Strip outer braces and parse inside
                            first_set = parse(expr[1:i])
                            rest_expr = expr[i + 1:]
                            break
                            
            if not rest_expr:
                return first_set
                
            # Cartesian product of first_set and parse(rest_expr)
            rest_set = parse(rest_expr)
            return {a + b for a, b in itertools.product(first_set, rest_set)}

        # Evaluate and return sorted list of unique words
        return sorted(list(parse(expression)))