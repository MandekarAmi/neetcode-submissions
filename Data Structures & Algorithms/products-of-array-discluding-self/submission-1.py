class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        prod0 = 1
        flag_one_0 = 0
        for num in nums:
            if num == 0:
                if flag_one_0 > 0:
                    flag_one_0 = flag_one_0 + 1
                    prod = 0
                    break
                else:
                    flag_one_0 = 1
                    continue
            prod = prod * num
        if flag_one_0 > 0:
            prod0 = prod
            prod = 0

        for num in nums:
            if num == 0:
                if flag_one_0 > 0:
                    res.append(prod0)
                    continue
                else:
                    res.append(0)
            res.append(int(prod/num))
        return res
