class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = (r+l//2)
        print(f'l={l}, r={r}, mid={mid}')
        while l<= r:
            print(f'l={l}, r={r}, mid={mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
            mid = (l+r)//2
        
        return -1

