class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        valid = {'(' : ')', '{' : '}', '[' : ']'}
        seen = []
        for c in s:
            if c in valid:
                seen.append(c)   
            elif len(seen) > 0 and c is valid[seen[-1]]:
                seen.pop()
            else:
                return False
        return True if not seen else False
