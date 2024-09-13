from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
"""
        Target: 44

          0  1  2  3  4  5
        [-1, 0, 3, 5, 9, 12]
mid:                      |
left:                        |
right:                    |
"""

nums = [-1,0,3,5,9,12]
target = 44

s = Solution()
res = s.search(nums, target)
print(res)