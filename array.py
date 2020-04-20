class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        l为零指针
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
            r += 1

        return nums

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        旋转矩阵
        """
        n = len(matrix)
        i, j = 0, n - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda val: val[0])
        result = []
        left = intervals[0][0]
        right = intervals[0][1]

        print(intervals)
        for i in range(1, n):
            if intervals[i][0] > right:
                result.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                right = max(right, intervals[i][1])

            if i == len(intervals) - 1:
                result.append([left, right])

        return result


if __name__ == '__main__':
    s = Solution()
    array = [[8, 9], [1, 2], [3, 10]]
    print(s.merge(array))