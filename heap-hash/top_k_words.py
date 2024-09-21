from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_and_count = Counter(sorted(words))
        top_words = [word[0] for word in words_and_count.most_common(k)]

        return top_words


words = ["i","love","leetcode","i","love","coding"]
k = 3

s = Solution()
res = s.topKFrequent(words, k)
print(res)
