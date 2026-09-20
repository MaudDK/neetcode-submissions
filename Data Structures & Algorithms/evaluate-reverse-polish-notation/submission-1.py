class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buffer = []
        for op in tokens:
            if op == '+':
                buffer.append(buffer.pop() + buffer.pop())

            elif op == '-':
                a, b = buffer.pop(), buffer.pop()
                buffer.append(b-a)

            elif op == '*':
                buffer.append(buffer.pop() * buffer.pop())
            
            elif op == '/':
                a, b = buffer.pop(), buffer.pop()
                buffer.append(int(b/a))
            
            else:
                buffer.append(int(op))
        
        return buffer[0]