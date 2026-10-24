class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd
            res+=self.countSub(i,i,s)
            # even
            res+=self.countSub(i,i+1,s)

        return res

    def countSub(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
        return res