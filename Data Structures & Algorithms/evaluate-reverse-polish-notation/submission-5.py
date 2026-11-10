
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if token == "+":
                    stack.append(n1 + n2)
                elif token == "-":
                    stack.append(n1 - n2)
                elif token == "*":
                    stack.append(n1 * n2)
                elif token == "/":
                    stack.append(int(n1 / n2))
                else:
                    raise ValueError(f"Unkown token: {token}")
        return stack.pop()