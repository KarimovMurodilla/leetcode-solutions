from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for _ in nums:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]


nums = [1, 2, 2, 0, 8]

s = Solution()
res = s.sortColors(nums)
# print(res)
print(nums)
