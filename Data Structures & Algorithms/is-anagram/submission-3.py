class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            s_seen = dict.fromkeys(set(s),0)
            # Count all letters in s
            for n in s:
                s_seen[n] += 1
            
            # Compare to t
        
            for m in t:
                if s_seen.get(m) is None or s_seen[m] == 0:
                    return False
                else:
                    s_seen[m] -= 1
            return True
        return False

         