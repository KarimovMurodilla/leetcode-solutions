from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        sorted_nums = sorted(list(set(nums)))
        count = 0
        max_count = 0
        next_num = sorted_nums[0]

        for num in sorted_nums:
            if num == next_num:
                count += 1
            else:
                next_num = num
                count = 1

            if count > max_count:
                max_count = count

            next_num += 1
        
        return max_count


nums = [0,3,7,2,5,8,4,6,0,1]

s = Solution()
result = s.longestConsecutive(nums)
print(result)
