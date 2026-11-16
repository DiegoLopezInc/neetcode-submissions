class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str_s = sorted(s, key=str.lower)
        str_t = sorted(t, key=str.lower)
        
        for i in range(len(s)):
            if str_s[i] != str_t[i]:
                return False


        return True
