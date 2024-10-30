from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        left = right = 0

        while right < len(nums):
            # pop less values from left
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            # remove if not in range
            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1

        return output
            

"""
nums = [1,3,-1,-3,5,3,6,7], k = 3

While right reaches k            Status
---------------------            -------
[1]  3  -1  -3  5  3  6  7       pending
[1  3]  -1  -3  5  3  6  7       pending
[1  3  -1]  -3  5  3  6  7       3 <- k reached by right

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

nums = [7,2,4]
k = 2

s = Solution()
res = s.maxSlidingWindow(nums, k)
print(res)