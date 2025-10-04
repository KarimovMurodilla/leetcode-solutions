from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        result = ""
        for word in words:
            result += word
            if result == s:
                return True
            
        return False



string = "aaa"
words = ["aa","love","leetcode","apples"]

s = Solution()
res = s.isPrefixString(string, words)
print(res)
