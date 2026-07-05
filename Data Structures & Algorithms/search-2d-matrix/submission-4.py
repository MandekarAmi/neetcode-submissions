class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums)-1
        mid = (l+r)//2
        if nums[mid] == target:
                return True 
        while l <= r:
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
            mid = (l+r)//2
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix)-1, len(matrix[0])-1
        if m == 0:
            return self.binary_search(matrix[0], target)
        for i in range(m+1):
            if target >= matrix[i][0] and target <= matrix[i][n]:
                if self.binary_search(matrix[i], target):
                    return True          
        return False
