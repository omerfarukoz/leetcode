class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(tokens):
            stack = []
            num = 0
            sign = 1
            total = 0
            i = 0
            op = '+'
            
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                if s[i] in '+-*/' or i == len(s) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))  # Use integer division
                    num = 0
                    op = s[i]
                i += 1
            
            return sum(stack)
        
        return evaluate(s)
