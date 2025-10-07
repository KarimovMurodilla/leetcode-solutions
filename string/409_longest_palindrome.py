from collections import Counter


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        counts = Counter(s)
        # even_len = 0
        # max_odd = 0

        # odds = []

        # for key in counts:
        #     if counts[key] % 2 == 0:
        #         even_len += counts[key]

        #     else:
        #         odds.append(counts[key])
        #         if counts[key] > max_odd:
        #             max_odd = counts[key]
        
        # if odds:
        #     # odds.remove(max(odds))
        #     even_len += (sum(odds) - max(odds)) - (len(odds)-1)
        # return even_len + max_odd

        answer = 0
        odd_found = False

        for count in counts.values():
            if count % 2 == 0:
                answer += count

            else:
                answer += count - 1
                odd_found = True

        if odd_found:
            answer += 1

        return answer


s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
sol = Solution()
res = sol.minimizedStringLength(s)
print(res)
