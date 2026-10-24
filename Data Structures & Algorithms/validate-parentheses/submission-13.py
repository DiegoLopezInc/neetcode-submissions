class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']': '[' }
        seen = []
        for c in s:
            if c in valid:
                if seen and seen[-1] == valid[c]:
                    seen.pop()
                else:
                    return False
            else:
                if c in valid.values():
                    seen.append(c)
                else:
                    return False

        res = True if not seen else False
        return res
