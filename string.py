class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        删除字符串重复元素
        """
        stack = []
        for s in S:
            append = 1
            while stack and stack[-1] == s:
                stack.pop()
                append = 0
            if append:
                stack.append(s)
        return ''.join(stack)

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        symbols = ['+', '-']
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        list_str = str.strip(' ')
        list_number = []

        for i, s in enumerate(list_str):
            if i == 0:
                if s.isdigit() or s in symbols:
                    list_number.append(s)
                    continue
                else:
                    return 0
            if s.isdigit():
                list_number.append(s)
            else:
                break

        result = 0
        symbol = False
        for i, num in enumerate(list_number):
            if i == 0:
                if num not in symbols:
                    result = int(num)
                else:
                    symbol = True
            else:
                result = result*10 + int(num)

        if symbol and list_number[0] == '-':
            result = -result

        if result > INT_MAX:
            result = INT_MAX
        if result < INT_MIN:
            result = INT_MIN

        return max(min(result, INT_MAX), INT_MIN)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = []
        for i in s:
            if i is ' ':
                if len(stack) != 0:
                    res = ''.join(stack)
                    result.insert(0, res)
                    stack = []
            else:
                stack.append(i)

        if len(stack) != 0:
            res = ''.join(stack)
            result.insert(0, res)

        return ' '.join(result)

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 扫描整数
        def scanInterger(index, s):
            if s[index] in ['+', '-']:
                index += 1
            return scanUnsignedInterger(index, s)

        def scanUnsignedInterger(index, s):
            pre = index
            while index < len(s) and '0' <= s[index] <= '9':
                index += 1
            return index > pre, index

        s = s.strip(' ')
        index = 0
        if s == '':
            return False

        number, index = scanInterger(index, s)

        if index > len(s) - 1:
            return number

        if index < len(s) and s[index] == '.':
            index += 1
            if index > len(s) - 1:
                return number
            res, index = scanUnsignedInterger(index, s)
            number = number or res

        if index < len(s) and s[index] in ['e', 'E']:
            index += 1
            if index > len(s) - 1:
                return False
            res, index = scanInterger(index, s)
            number = number and res

        if index < len(s):
            return False
        return number


if __name__ == '__main__':
    s = Solution()
    # print([s.reverseWords("blue is sky the")])
    # print(s.isNumber('-1E-16'))
    a = 'ab'
    b = 'abc'
    if a in b:
        print(a)