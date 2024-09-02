from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result ^= number
            print(result)
        return result

nums = [4,2,2,3,3]
s = Solution()
res = s.singleNumber(nums)
print(res)