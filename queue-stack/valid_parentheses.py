class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        expectations = []

        for i in s:
            if i in brackets.values() and i not in expectations:
                return False

            elif i in brackets.keys():
                expectations.append(brackets[i])
            
            elif i == expectations[-1]:
                expectations.pop()
        
        return False if expectations else True
