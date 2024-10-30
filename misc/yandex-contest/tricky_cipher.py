
class Solution:
    def cipher(self, count: int):
        final_result = ''

        for _ in range(count):
            data = input().split(',')
            count_char = len(set("".join(data[:3])))
            day_month = "".join([data[3], data[4]])
            sum_day_month = sum([int(n) for n in day_month])
            char_num = ord(data[0].lower()[0]) - 96
            pre_result = hex(count_char + sum_day_month * 64 + char_num * 256)
            result = pre_result[-3:] if len(pre_result[2:]) >= 3 else '0'*(3-len(pre_result[2:])) + pre_result[2:]
            result += ' '
            final_result += result

        return final_result.upper().strip()



# count = int(input())

# s = Solution()
# res = s.cipher(count)
# print(res)


def sixteen(num):
    letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    res = []
    while num != 0:
        if num % 16 < 10:
            res.append(num % 16)
        else:
            res.append(letters[num % 16])
        num //= 16
    ans = res[:3][::-1] if len(res) >= 3 else str(0 * (3 - len(res))) + str(res[::-1])
    return ''.join(str(el) for el in ans)


def cipher(data):
    res = []
    for el in data:
        unique_letters = len(set(el[0] + el[1] + el[2]))
        day_plus_month = sum([int(ch) for ch in el[3]]) + sum([int(ch) for ch in el[4]])
        surname_letter = ord(el[0][0].lower()) - ord('a') + 1
        ciphernum = surname_letter * 256 + unique_letters + 64 * day_plus_month

        print("count char:", unique_letters)
        print("sum day month:", day_plus_month)
        print("char num:", surname_letter)
        print("pre result:", ciphernum)
        
        res.append(sixteen(ciphernum))
    return res


data = []

count = int(input())

# for i in range(count):
#     data.append(input().split(','))

# res = cipher(data)
# print(' '.join(res))


s = Solution()
res = s.cipher(count)
print(res)
