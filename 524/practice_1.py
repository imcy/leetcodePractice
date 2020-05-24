class Solution(object):
    def isPalindrome(self, x):
        x_c = str(x)
        return x_c == x_c[::-1]

    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        dp = [[True for i in range(n)] for i in range(n)]

        start, max_len = 0, 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j] is True:
                    cur_len = j - i + 1
                    if cur_len >= max_len:
                        max_len = cur_len
                        start = i
        return s[start: start+max_len]

    def maxProduct(self, nums):
        if len(nums) == 0:
            return
        imax, imin = 1, 1
        res = -2**31
        for i in range(0, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(nums[i]*imax, nums[i])
            imin = min(nums[i]*imin, nums[i])
            res = max(imax, res)

        return res

    def checkSubarraySum(self, nums, k):
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] and nums[i] == 0:
                    return True
            return False

        preSum = [0 for i in range(len(nums)+1)]
        int_map = {}
        for i in range(1, len(nums)+1):
            preSum[i] = preSum[i-1] + nums[i-1]
            index = preSum[i] % k
            if not int_map.get(index):
                int_map[index] = []
            int_map[index].append(i)

        if not int_map.get(preSum[0] % k):
            int_map[preSum[0] % k] = []
        int_map[preSum[0] % k].append(0)

        for i in range(1, len(nums)+1):
            index = preSum[i] % k
            for j in int_map[index]:
                if j < i - 1:
                    return True
        return False

    def waysToChange(self, n):
        # dp[i] = (dp[i] + dp[i - coin])
        coins = [1, 5, 10, 25]
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[n] % 1000000007

    def coinChange(self, coins, amount):
        # dp[i] = min(dp[i], dp[i-c] + 1)
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def minCount(self, coins):
        count = 0
        for coin in coins:
            count += coin // 2 + coin % 2
        return count

    def change(self, amount, coins):
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = dp[j] + dp[j-coin]
        return dp[amount]

    def permutation(self, S):
        S = sorted(S)
        result = []
        res_ = []
        n = len(S)
        visited = [False for _ in range(n)]

        def dfs(i):
            if i == n:
                string = ''.join(res_)
                result.append(string)
                return
            for j in range(0, n):
                if not visited[j]:
                    if j > 0 and S[j] == S[j-1] and visited[j-1] is False:
                        continue
                    res_.append(S[j])
                    visited[j] = True
                    dfs(i+1)
                    visited[j] = False
                    res_.pop()

        dfs(0)

        return result

    def generateParenthesis(self, n):
        result = []

        def dfs(left, right, res):
            if len(res) == n * 2:
                result.append(''.join(res))
            if left < n:
                dfs(left + 1, right, res + ['('])
            if right < left:
                dfs(left, right + 1, res + [')'])

        dfs(0, 0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))