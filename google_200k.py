"""
1. Set last num
2. Do all operations with last and current num: +-*/
3. Append to list result
4. Get max number from list
"""

from typing import List

class Solution:
    def findOptimal(self, nums: List):
        last_num = None
        max_num = 0
        min_num = 0

        for i in nums:
            if not last_num:
                last_num = i
                max_num = i
                min_num = i
            
            else:
                add_num_max = max_num + i
                sub_num_max = max_num - i
                mul_num_max = max_num * i
                div_num_max = max_num / i

                add_num_min = min_num + i
                sub_num_min = min_num - i
                mul_num_min = min_num * i
                div_num_min = min_num / i

                all_max = [add_num_max, sub_num_max, mul_num_max, div_num_max]
                all_min = [add_num_min, sub_num_min, mul_num_min, div_num_min]

                max_num = max(all_max)
                min_num = min(all_min)

                all_nums = all_max + all_min
                last_num = max(all_nums)

        return last_num
    

nums = [1, -3, 0.1, -5]
s = Solution()
res = s.findOptimal(nums)

print(res)