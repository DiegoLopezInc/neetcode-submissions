class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for n in s:
            if n.isalnum():
                if n.isalpha():
                    clean.append(n.lower())
                    continue
                clean.append(n)
        
        cleaned = ''.join(clean)

        p1 = 0
        p2 = len(cleaned) - 1
        while p1 < p2:
            if cleaned[p1] != cleaned[p2]:
                return False
            p1+=1
            p2-=1
        return True