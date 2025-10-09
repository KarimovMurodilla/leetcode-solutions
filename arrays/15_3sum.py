from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif three_sum < 0:
                    left += 1

                else:
                    right -= 1

        return result

 
# nums = [-1,0,1,2,-1,-4]
nums = [-2, 0, 0, 2, 2]

s = Solution()
res = s.threeSum(nums)
print(res)


"""
  |
[-4, -1, -1, 0, 1, 2]



"""
