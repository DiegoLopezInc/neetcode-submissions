class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd
            l = r = i
            res+=self.countSub(l,r,s)

            # even
            l,r = i,i+1
            res+=self.countSub(l,r,s)

        return res

    def countSub(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
        return res