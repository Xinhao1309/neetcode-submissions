class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if c == ")" and popped != "(":
                    return False
                elif c == "}" and popped != "{":
                    return False
                elif c == "]" and popped != "[":
                    return False
                elif c in [")", "}", "]"]:
                    continue
                else:
                    return False
        if not stack:
            return True
        return False