class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                # print(f"{stack} {token}")
                val = self.eval(stack, token)
                stack.pop()
                stack.pop()
                stack.append(val)
        return int(stack[-1])

    def eval(self, stack: List[int], op: str) -> int:
        r = int(stack[-1])
        l = int(stack[-2])
        res = 0
        if op == "+":
            res = l + r
        if op == "-":
            res = l - r
        if op == "*":
            res = l * r
        if op == "/":
            res = l / r
        return res                