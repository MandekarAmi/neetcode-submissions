import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)

        if len(nums) == 0:
            return 0

        max_l = 1
        for n in nums:
            if n-1 in store:
                continue
            if n+1 in store:
                k = n+1
                while k-n+1 < len(store):
                    if k + 1 not in store:
                        break
                    k = k + 1
                max_l = max(max_l, k-n+1)
        return max_l
