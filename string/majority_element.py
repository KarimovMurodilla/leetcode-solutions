from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
    

nums = [2,2,1,1,1,2,2]
s = Solution()
res = s.majorityElement(nums)
print(res)
