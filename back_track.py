class Solution(object):

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        机器人移动路径
        """
        if m < 1 or n < 1 or k < 0:
            return 0
        visited = [False for _ in range(m * n)]

        def get_sum(n):
            sums = 0
            while n:
                sums += n % 10
                n = n // 10
            return sums

        def moving(x, y):
            cnt = 0
            if 0 <= x < n and 0 <= y < m and not visited[y * n + x]:
                visited[y * n + x] = True
                if get_sum(x) + get_sum(y) <= k:
                    cnt = 1 + moving(x + 1, y) + moving(x - 1, y) \
                          + moving(x, y + 1) + moving(x, y - 1)

            return cnt

        return moving(0, 0)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        全排列1
        """
        result = []
        res_ = []
        visited = [False for _ in range(len(nums))]
        n = len(nums)

        def dfs(i):
            if i == n:
                result.append(res_.copy())
                return
            else:
                for j in range(0, n):
                    if not visited[j]:
                        res_.append(nums[j])
                        visited[j] = True
                        dfs(i + 1)
                        visited[j] = False
                        res_.pop()

        dfs(0)
        return result

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        全排列2
        """
        result = []
        res_ = []
        visited = [False for _ in range(len(nums))]
        n = len(nums)

        def dfs(i):
            if i == n:
                result.append(res_.copy())
                return
            else:
                for j in range(0, n):
                    if not visited[j]:
                        if j > 0 and nums[j] == nums[j - 1] and visited[j - 1] is False:
                            continue
                        res_.append(nums[j])
                        visited[j] = True
                        dfs(i + 1)
                        visited[j] = False
                        res_.pop()

        dfs(0)
        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        res = []

        def dfs(left_count, right_count):
            if len(res) == 2 * n:
                result.append(''.join(res))
                return
            if left_count < n:
                res.append('(')
                dfs(left_count + 1, right_count)
                res.pop()

            if right_count < left_count:
                res.append(')')
                dfs(left_count, right_count + 1)
                res.pop()

        dfs(0, 0)
        return result

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        def dfs(x, y):
            visited[x][y] = True
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] is False and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    count += 1
                    dfs(i, j)
        return count

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

    def letterCasePermutation(self, S):
        result = []

        def dfs(s, res_):
            if len(s) == 0:
                result.append(''.join(res_))
                return
            if s[0].isalpha():
                dfs(s[1:], res_ + [s[0].upper()])
                dfs(s[1:], res_ + [s[0].lower()])
            else:
                dfs(s[1:], res_ + [s[0]])

        dfs(S, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))
