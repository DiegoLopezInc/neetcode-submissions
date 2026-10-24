class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge Cases
        if len(strs) == 0:
            return []        

        # count dict
        seen = {}
        sublists = {} # This will store all signature: list mappings globally

        for word in strs:
            # count using a signature of alphabet
            signature = [0] * 26
            for letter in word:
                # count each letter using alphabetical index
                signature[ord(letter) - ord('a')] += 1    
            
            save = tuple(signature)
            # store using len to sublist with same signture
            size = len(word)
            if seen.get(size) is None:
                seen[size] = {}

            # nest sublists
            # add new word to sublist
            if seen[size].get(save) is not None:
                seen[size][save].append(word)
            else:
                seen[size][save] = [word]

        # store sublists using len as key
        # store as immutible
        # retrieve sublists in sublists
        output = []
        for size_dict in seen.values():
            for sublist in size_dict.values():
                output.append(sublist)

        return output