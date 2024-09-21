from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        last_price = prices[0]

        for i in prices:
            if last_price > i:
                last_price = i
            else:
                new_price = i - last_price
                max_price = max(max_price, new_price)

        return max_price
    

prices = [7,1,5,3,6,4]
s = Solution()
res = s.maxProfit(prices)
print(res)
