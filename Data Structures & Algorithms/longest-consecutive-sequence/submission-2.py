import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        if len(nums) == 1:
            return 1

        max_res = []
        working_res = []
        while len(nums) > 0:
            i = heapq.heappop(nums)
            lw = len(working_res)
            if lw > 0:
                if working_res[-1] == i:
                    continue
                if working_res[-1] == i-1:
                    working_res.append(i)
                else:
                    working_res = [i]
            else:
                working_res.append(i)
            print(working_res)
            if len(working_res) > len(max_res):
                max_res = working_res
        return len(max_res)

                
            
