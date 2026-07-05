import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add, 
            "*": operator.mul, 
            "-": operator.sub, 
            "/": operator.truediv
        }
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                op_func = operators.get(token)
                result = op_func(num1, num2)
                stack.append(int(result))
            else:
                stack.append(int(token))
        
        return stack[0]
        