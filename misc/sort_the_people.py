from typing import List

class Solution:
    def get_second(self, x: tuple):
        return x[1]

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = []
        for name, height in zip(names, heights):
            data.append((name, height))

        sorted_data = sorted(data, key=self.get_second, reverse=True)
        names = [name[0] for name in sorted_data]

        return names
    

names = ["Alice","Bob","Bob"]
heights = [155,185,150]

s = Solution()
res = s.sortPeople(names, heights)
print(res)
