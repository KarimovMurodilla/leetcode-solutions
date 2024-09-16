from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        last_val = -10001
        rotated_index = 0

        for i in range(len(nums)):
            if nums[i] < last_val:
                rotated_index = i
                break
            last_val = nums[i]

        if rotated_index == 0:
            return self.binary_search(nums, target)
        
        else:
            left = self.binary_search(nums[rotated_index:], target)
            right = self.binary_search(nums[:rotated_index], target)

            if left == -1 and right == -1:
                return -1
            elif left != -1:
                return len(nums[:rotated_index]) + left
            else:
                return right


nums = [4,5,6,7,0,1,2]
target = 0

s = Solution()
res = s.search(nums, target)
print(res)