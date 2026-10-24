class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        valid = {'(' : ')', '{' : '}', '[' : ']'}
        seen = []
        for c in s:
            if c in valid:
                seen.append(c)   
            elif len(seen) > 0 and c in valid[seen[-1]]:
                seen.pop()
            else:
                return False

        if len(seen) == 0:
            return True
        return False
