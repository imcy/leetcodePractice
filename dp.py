import sys


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        爬楼梯问题
        初始化：
            dp[]=[1,2]
        转移：
            dp[i] = dp[i-1]+dp[i-2]
        """
        record_list = [1, 2]
        if n < 3:
            return record_list[n - 1]
        for i in range(2, n):
            res = record_list[0] + record_list[1]
            record_list[0] = record_list[1]
            record_list[1] = res

        return record_list[1]

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最大子序列和
        f(n) = max(f(n-1)+nums[n], nums[n])
        """
        if len(nums) == 0:
            return
        f_n = -1
        res = -2 ** 31
        for i in range(0, len(nums)):
            f_n = max(f_n + nums[i], nums[i])
            res = max(res, f_n)
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        最长回文子串
        初始化：
            dp[i][j] = true
        状态：
            dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
        """
        len_s = len(s)
        if len_s < 2:
            return s
        dp = [[True for i in range(len_s)] for i in range(len_s)]
        start, max_len = 0, 1
        for i in range(len_s - 1, -1, -1):
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] is True:
                    cur_len = j - i + 1
                    if max_len < cur_len:
                        start = i
                        max_len = cur_len

        return s[start:start + max_len]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        最长回文子串长度
        初始化：
        dp[i][i] = 1
        转移：
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        """
        len_s = len(s)
        dp = [[0 for i in range(len_s)] for i in range(len_s)]

        for i in range(len_s - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len_s - 1]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        j - c < j
        01背包：
        dp[i][j] = min(dp[i-1]dp[j], dp[i-1][j-c]+1)
        从大到小：dp[j] = min(dp[j], dp[j-c] + 1)
        完全背包：
        dp[i][j] = min(dp[i-1]dp[j], dp[i][j-c]+1)
        从小到大：dp[j] = min(dp[j], dp[j-c] + 1)
        """
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def maxBag(self, w, v, m):
        """

        :param w:
        :param v:
        :param m:
        :return:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i]+v_i)
        简化, 从大到小：
        dp[j] = max(dp[j], dp[j-w_i]+v_i)
        """
        # len_s = len(w)
        # dp = [[0 for i in range(m+1)] for i in range(len_s)]
        #
        # for i in range(0, len_s):
        #     for j in range(1, m+1):
        #         if i == 0:
        #             if j-w[i] >= 0:
        #                 dp[i][j] = v[i]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        #             if j - w[i] >= 0:
        #                 dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]]+v[i])
        # return dp[len_s-1][m]
        dp = [0 for i in range(m + 1)]
        for i, w_i in enumerate(w):
            for j in range(m, w_i - 1, -1):
                dp[j] = max(dp[j], dp[j - w_i] + v[i])
        return dp[m]

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        三角形最大路径
        转移公式：
        if j == 0:
            dp[j] = dp[j] + t[j]
        elif j == len(t) - 1:
            dp[j] = dp[len(t)-2] + t[j]
        else:
            dp[j] = min(dp[j - 1], dp[j]) + t[j]

        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return
        # dp = [[0 for i in range(len(triangle[i]))] for i in range(len(triangle))]
        # for i, t in enumerate(triangle):
        #     if i == 0:
        #         dp[0][0] = t[0]
        #     else:
        #         for j in range(len(t)):
        #             if j == 0:
        #                 dp[i][j] = dp[i-1][0] + t[j]
        #             elif j == len(t) - 1:
        #                 dp[i][j] = dp[i-1][-1] + t[j]
        #             else:
        #                 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + t[j]
        #
        # return min(dp[len(triangle)-1])

        dp = [0 for i in range(len(triangle[-1]))]
        min_path = None
        for i, t in enumerate(triangle):
            min_path = 2 ** 31 - 1
            if i == 0:
                dp[0] = t[0]
                min_path = min(min_path, dp[0])
            else:
                for j in range(len(t) - 1, -1, -1):
                    if j == 0:
                        dp[j] = dp[j] + t[j]
                    elif j == len(t) - 1:
                        dp[j] = dp[len(t) - 2] + t[j]
                    else:
                        dp[j] = min(dp[j - 1], dp[j]) + t[j]
                    min_path = min(min_path, dp[j])
        return min_path

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最大子序列乘机
        维护最小和最大，出现负数时交换最小和最大
        f(n) = max(f(n-1)+nums[n], nums[n])
        """
        if len(nums) == 0:
            return
        imax, imin = 1, 1
        res = -2 ** 31
        for i in range(0, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            res = max(res, imax)
        return res

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        偷：
        dp[i] = dp[i-2]+nums[i]
        不偷：
        dp[i] = dp[i-1]

        dp[i] = max(dp[i-1], dp[i-2]+nums[i]

        dp[n+1] = max(dp[n], dp[n-1]+num)
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        dp = [0 for i in range(len(nums) + 1)]
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        第一个最后相邻
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        return max(self.rob(nums[1:]), self.rob(nums[:-1]))

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        猜数字最小花费，k代表pick的数字，dp[j][i]为区间内最小花费
        dp[j][i] = globalmin(k + max(dp[j][k-1], dp[k+1][i])) : k in range(j, i)
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                global_min = 2 ** 31 - 1
                for k in range(j, i):
                    local_max = k + max(dp[j][k - 1], dp[k + 1][i])
                    global_min = min(global_min, local_max)
                dp[j][i] = global_min
        return dp[1][n]

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        第一维：楼层数，第二维鸡蛋个数
        dp[n][1] = n

        碎掉：dp[k][j]=dp[k-1][j-1]
        不碎：dp[k][j]=dp[i-k][j]

        dp[i][j]=localmin(max(dp[k-1][j-1], dp[i-k][j]+1))
        """

        # dp = [[0]*(K+1) for i in range(N+1)]
        # for i in range(1, N + 1):
        #     for j in range(K + 1):
        #         if i == 1:
        #             dp[i][j] = 1
        #             continue
        #         if j == 0:
        #             dp[i][0] = 0
        #             continue
        #         if j == 1:
        #             dp[i][1] = i
        #             continue
        #         # globalmin = 2**31
        #         # for k in range(1, i+1):
        #         #     localmax = max(dp[k-1][j-1], dp[i-k][j])+1
        #         #     globalmin = min(localmax, globalmin)
        #         left, right = 1, i
        #         while left < right:
        #             mid = left + (right - left + 1)//2
        #             t1 = dp[mid-1][j-1]
        #             t2 = dp[i-mid][j]
        #             if t1 > t2:
        #                 right = mid - 1
        #             else:
        #                 left = mid
        #         dp[i][j] = max(dp[left-1][j-1], dp[i-left][j])+1
        # return dp[N][K]
        # k为鸡蛋，n为楼层
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)

    def waysToChange(self, n):
        # dp[i] = (dp[i] + dp[i - coin])
        coins = [1, 5, 10, 25]
        dp = [0 for i in range(n+1)]

        for coin in coins:
            for i in range(coin, n):
                dp[i] = dp[i] + dp[i-coin]
        return dp[n] % 1000000007

    def pileBox(self, box):
        # 能堆到最大上面：dp[i] = maxhi + box[i][2]
        # 不能堆dp[i]=box[i][2]，找能堆的：dp[i] = max(dp[k]+box[i][2], dp[i])
        def helper(b1, b2):
            for j in range(3):
                if b1[j] <= b2[j]:
                    return False
            return True

        box.sort()
        dp = [0 for _ in range(len(box))]
        dp[0] = box[0][2]
        maxhi = dp[0]
        maxbox = box[0]
        for i in range(1, len(box)):
            canpile = helper(box[i], maxbox)
            if canpile:
                dp[i] = maxhi + box[i][2]

            else:
                dp[i] = box[i][2]
                for k in range(i):
                    canpile2 = helper(box[i], box[k])
                    if canpile2:
                        dp[i] = max(dp[i], dp[k]+box[i][2])

            if dp[i] > maxhi:
                maxhi = dp[i]
                maxbox = box[i]

        return maxhi


if __name__ == '__main__':
    s = Solution()
    print(s.pileBox([[2, 3, 4], [4, 6, 8]]))
