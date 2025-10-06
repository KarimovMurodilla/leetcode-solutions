from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = sorted(nums)
        return res


nums = [1,0,-1,0,-2,2]
target = 0

s = Solution()
res = s.fourSum(nums, target)
print(res)
