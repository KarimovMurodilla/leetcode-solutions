class Solution:
    def twoSum(self, nums: list, target: int):
        d = {}
        
        for i, k in enumerate(nums):
            if target - k in d:
                return [d[target-k], i]

            elif k not in d:
                d[k] = i


nums = [2,7,11,15]
target = 9

s = Solution()
res = s.twoSum(nums, target)
print(res)