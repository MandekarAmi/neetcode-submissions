class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if numbers[i] in seen.keys():
                return [seen[numbers[i]]+1, i+1]
            seen[comp] = i
        return [-1,-1]