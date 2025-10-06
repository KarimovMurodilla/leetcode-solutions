from typing import List
from collections import defaultdict

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for letter in i:
                count[ord(letter) - ord("a")] += 1
            
            result[tuple(count)].append(i)

        return list(result.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
res = s.groupAnagrams(strs)
print(res)