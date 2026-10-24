class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # count frequent elements
        count = {}
        for n in nums:
            if count.get(n) is None:
                count[n] = 1
            else:
                count[n] += 1
            
        # save least to most frequent n as a list 
        # sort list


        # create return list and pop from sorted
        elements = []
        while count and k > 0:
            max_key = max(count , key=count.get)
            elements.append(max_key)
            count.pop(max_key)
            k-=1
        
        return elements
            