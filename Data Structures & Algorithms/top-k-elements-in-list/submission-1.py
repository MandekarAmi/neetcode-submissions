class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] = freq_map[n] + 1
            else:
                freq_map[n] = 1

        sorted_dict = dict(sorted(freq_map.items(), reverse= True, key=lambda item: item[1]))
        return list(sorted_dict)[:k]
        
        