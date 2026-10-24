class Solution:
    def countSubstrings(self, s: str) -> int:
        res = set()


        for i in range(len(s)):
            # odd
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (l,r) in res:
                    continue
                else:
                    res.add((l,r))
                l-=1
                r+=1

            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (l,r) in res:
                    continue
                else:
                    res.add((l,r))
                l-=1
                r+=1

        return len(res)
            