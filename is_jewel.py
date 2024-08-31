class Solution:
    def is_jewel(self, stones: str, jewels: str):
        return len(set(stones).intersection(jewels))
        
    

jewels = "aA" # a — бриллиант, A – сапфир
stones = "aAAbbbb" # b — кварц (недрагоценный)

s = Solution()
res = s.is_jewel(stones, jewels)
print(res)
