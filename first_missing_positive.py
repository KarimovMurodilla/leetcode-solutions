"""
1. Listni sort qilib olasiz; takrorlanadigan elementlar bo'lmasligi kerak; 1 dan kichik bo'lgan sonlarni listni 
ohiriga joylashtirasiz
2. for bilan tartiblangan listni birin ketin tekshirib chiqasiz indexi orqali, agar nums[i] != i bo'lsa, i missing positive integer hisoblanadi.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:        
        nums = sorted(set(nums), key=lambda x: x if x > 0 else float("inf"))

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
            if nums[i] == nums[-1]:
                return nums[i] + 1
            
nums = [0,1,2]
s = Solution()
res = s.firstMissingPositive(nums)
print(res)