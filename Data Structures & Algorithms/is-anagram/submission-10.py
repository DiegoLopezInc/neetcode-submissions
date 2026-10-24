class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}

        for c in s:
            if c in seen:
                seen[c]+=1
            else:
                seen[c]=1
        
        for c in t:
            if c not in seen:
                return False
            if seen.get(c) == 0:
                return False
            if c in seen:
                seen[c]-=1
        
        return True
