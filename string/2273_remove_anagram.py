from copy import copy
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        a = 0
        b = 1

        d = {0: words[0]}

        while b < len(words):
            if sorted(words[a]) == sorted(words[b]):
                b += 1
            else:
                d[b] = words[b]
                a = b
                b += 1

        return list(d.values())


words = ["abba","baba","bbaa","cd","cd"]
s = Solution()
res = s.removeAnagrams(words)
print(res)
