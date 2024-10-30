class Solution:
    def min_swaps_to_group_ones(self, nums):
        n = len(nums)
        count_ones = sum(nums)
        
        if count_ones == 0 or count_ones == n:
            return 0
        
        extended_nums = nums * 2
        current_zeros = count_ones - sum(extended_nums[:count_ones])
        
        min_swaps = current_zeros
        
        for i in range(1, n):
            if extended_nums[i - 1] == 0:
                current_zeros -= 1
            if extended_nums[i + count_ones - 1] == 0:
                current_zeros += 1
            
            min_swaps = min(min_swaps, current_zeros)
        
        return min_swaps

num = int(input())
nums = list(map(int, input().split()))

s = Solution()
print(s.min_swaps_to_group_ones(nums))
