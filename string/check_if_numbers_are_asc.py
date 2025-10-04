class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(x) for x in s.split() if x.isdigit()]
        last_num = 0

        print(numbers)

        for num in numbers:
            if num > last_num:
                last_num = num

            else:
                return False
            
        return True
    

s = Solution()
string = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
res = s.areNumbersAscending(string)
print(res)
