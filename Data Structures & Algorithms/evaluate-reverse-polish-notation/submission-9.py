class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                last_item = stack.pop()       # Second operand
                second_last = stack.pop()     # First operand
                
                if token == '+':
                    res = second_last + last_item
                elif token == '-':
                    res = second_last - last_item
                elif token == '*':
                    res = second_last * last_item
                elif token == '/':
                    # int(a / b) truncates towards zero in Python 3
                    res = int(second_last / last_item)
                
                # Push result back onto the TOP of the stack (RIGHT side)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]