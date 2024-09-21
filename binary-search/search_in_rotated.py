from typing import List

"""
Base
1. if target == mid. success

Left portion (left <= mid)
1. if target > mid. go to right 
2. if target < mid and target < left. go to right 
3. if target >= left. go to left

Right portion
1. if target < mid. go to left
2. if target > mid and target > right. go to left
3. if target > mid and target < right. go to right 
"""


class Solution:   
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # Left portion
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Right portion
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


nums = [4,5,6,7,0,1,2]
target = 0

s = Solution()
res = s.search(nums, target)
print(res)