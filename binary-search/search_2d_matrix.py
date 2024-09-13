from typing import List

class Solution:
    def linear_search(self, nums: List[int], target: int) :
        for i in range(len(nums)):
            if i == target:
                return True
            
    def binary_search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if target > nums[-1]:
                continue

            res = self.linear_search(nums, target)
            if res:
                return True
            
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 232133

s = Solution()
res = s.searchMatrix(matrix, target)
print(res)