class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: int(float(x) / y)}
        
       
        i = 0
        stack = []
        while i < len(tokens):
            c = tokens[i] 
            if c not in operators:
                stack.append(int(c))
            if c in operators:
                r = stack.pop()
                l = stack.pop()
                res = operators[c](l, r)
                stack.append(res)
            i += 1


        
            
        return stack[0]
                    
