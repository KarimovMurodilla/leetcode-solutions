from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            sorted_word = set(word)
            is_ok = True
            for w in sorted_word:
                if w not in allowed:
                    is_ok = False
            
            if is_ok:
                count += 1

        return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
s = Solution()
res = s.countConsistentStrings(allowed, words)
print(res)
