from typing import List

from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        full_text = s1 + " " + s2
        full_text_list = full_text.split()

        result = []

        # for word in full_text_list:
        #     count = full_text_list.count(word)
        #     if count == 1:
        #         result.append(word)

        # return result

        counts = Counter(full_text_list)
        
        for key in counts:
            if counts[key] == 1:
                result.append(key)

        return result

s1 = "apple apple"
s2 = "banana"

s = Solution()
res = s.uncommonFromSentences(s1, s2)
print(res)
