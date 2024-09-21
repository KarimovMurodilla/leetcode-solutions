from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=float('inf')

        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            
            if(nums[mid] >= nums[left]):
                ans=min(ans, nums[left])
                left=mid+1
            
            else:
                ans=min(ans, nums[mid])
                right=mid-1
                  
        return ans
    

nums = [5, 6, 1, 2]
s = Solution()
res = s.findMin(nums)
print(res)