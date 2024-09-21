from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if nums[left] != nums[mid]:
                # Left portion 
                if nums[left] <= nums[mid]:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid] and target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                # Right portion
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    elif target > nums[mid] and target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                left += 1

        return False

"""
Target: 0

         0 1 2 3 4 5 6
        [2,5,6,0,0,1,2]
left:    |
middle:        | 
right:               |

target=1
[2,2,2,2,3,1,2,2,2,2,2]
"""
nums = [10,10,10,-10,-10,-10,-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,10,10]
target = 17171

s = Solution()
res = s.search(nums, target)
print(res)
