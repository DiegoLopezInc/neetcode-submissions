class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        seen = {}
        for n in s:
            if n in seen:
                seen[n]+=1
            else:
                seen[n] = 1


        for c in t:
            if c not in seen or seen.get(c) == 0:
                return False
            else:
                seen[c]-=1
        
        for v in seen.values():
            if v != 0:
                return False


        return True
