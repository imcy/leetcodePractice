class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window = {}
        need = {}

        for c in t:
            if need.get(c): need[c] += 1
            else: need[c] = 1

        left, right, valid = 0, 0, 0
        start, length = 0, 2**31-1

        while right < len(s):
            c = s[right]

            right += 1
            if need.get(c):
                if window.get(c): window[c] +=1
                else: window[c] = 1

                if window.get(c) == need.get(c):
                    valid += 1

            while valid == len(need):
                # 更新长度
                if right - left < length:
                    start = left
                    length = right - start

                # 移除
                d = s[left]
                left += 1
                if need.get(d):
                    if window.get(d) == need.get(d):
                        valid -= 1
                    window[d] -= 1

        print(length)
        if length <= len(s):
            return s[start:start+length]
        else:
            return ""


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("a", 'a'))

