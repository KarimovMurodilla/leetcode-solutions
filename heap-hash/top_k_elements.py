from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_and_count = Counter(words)
        top_words = [word[0] for word in words_and_count.most_common(k)]

        return top_words


nums = [1,1,1,2,2,3]
k = 2

s = Solution()
res = s.topKFrequent(nums, k)
print(res)
