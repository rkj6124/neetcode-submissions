class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = len(s)
        for i in range(l-1, -1, -1):
            print(stack)
            if stack and self.isClosing(stack[-1], s[i]):
                stack.pop()
                continue
            stack.append(s[i])

        if stack:
            return False
        return True

    def isClosing(self, top: str, ele: str):
        if top == "]" and ele == "[":
            return True
        if top == "}" and ele == "{":
            return True
        if top == ")" and ele == "(":
            return True
        return False