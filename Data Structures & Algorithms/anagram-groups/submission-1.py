class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, n in enumerate(strs):
            bucket = "".join(sorted(n))

            if bucket in seen:
                if self.valid_anagram(seen[bucket][-1], n):
                    seen[bucket].append(n)

            # What to do if first str is only non anagram?
            else:
                seen[bucket] = [n]

        return [x for x in seen.values()]
        
    def valid_anagram(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        b = sorted(s2)

        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        
        return True
        