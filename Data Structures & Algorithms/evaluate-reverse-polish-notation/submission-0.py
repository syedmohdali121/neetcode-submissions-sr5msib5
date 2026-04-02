class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                b = stack.pop() # The second operand
                a = stack.pop() # The first operand
                stack.append(a - b)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                # We use int() for division to strictly truncate toward zero.
                stack.append(int(a / b))
            else:
                # If it's not an operator, it must be a number
                stack.append(int(token))
                
        # The final result is the only item left in the stack
        return stack[0]