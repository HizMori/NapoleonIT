class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        m = list()
        for i in s:
            if i == 'I':
                m.append(1)
            if i == 'V':
                m.append(5)
            if i == 'X':
                m.append(10)
            if i == 'L':
                m.append(50)
            if i == 'C':
                m.append(100)
            if i == 'D':
                m.append(500)
            if i == 'M':
                m.append(1000)
        compare_number = 0
        number = 0
        for i in m:
            if compare_number >= i:
                number += i
            else:
                number += i - compare_number * 2
            compare_number = i
        return number
print(Solution().romanToInt(input()))