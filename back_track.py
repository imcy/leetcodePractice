class Solution(object):

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m < 1 or n < 1 or k < 0:
            return 0
        visited = [False for _ in range(m*n)]

        def get_sum(n):
            sums = 0
            while n:
                sums += n % 10
                n = n // 10
            return sums

        def moving(x, y):
            cnt = 0
            if 0 <= x < n and 0 <= y < m and not visited[y*n+x]:
                visited[y*n+x] = True
                if get_sum(x) + get_sum(y) <= k:
                    cnt = 1 + moving(x+1, y) + moving(x-1, y) \
                            + moving(x, y+1) + moving(x, y-1)

            return cnt

        return moving(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(3, 3, 2))
