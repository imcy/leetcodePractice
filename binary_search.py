class Solution(object):
    def binarySearch(self, arr, target):
        find = False
        left, middle, right = 0, -1, len(arr) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle] == target:
                find = True
                break
            elif target > arr[middle]:
                left = middle + 1
            else:
                right = middle - 1

        if find:
            return middle
        else:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        两次二分查找
        """
        if not nums: return [-1, -1]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle
        if nums[left] == target:
            lbound = left
        elif nums[right] == target:
            lbound = right
        else:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle
        if nums[right] == target:
            rbound = right
        elif nums[left] == target:
            rbound = left
        else:
            return [-1, -1]

        return [lbound, rbound]

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def conis(counter):
            sums = counter*(1+counter)//2
            return sums

        l, r = 0, n
        while l < r:
            m = l + (r - l + 1) // 2
            if conis(m) > n:
                r = m - 1
            else:
                l = m
        return l

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def guess(num):
            pick = 6
            if num > pick:
                return -1
            elif num < pick:
                return 1
            else:
                return 0

        left, right = 0, n
        while left <= right:
            middle = left + (right - left) // 2
            g = guess(middle)
            if g == -1:
                right = middle - 1
            elif g == 1:
                left = middle + 1
            else:
                return middle


if __name__ == '__main__':
    s = Solution()
    # arr = [2, 2]
    # print(s.guessNumber(10))
    string = '''[

  {

    "name":"张国立",

    "sex":"男",

    "email":"zhangguoli@123.com",

    "url":"./img/1.jpg"

  },

  {

    "name":"张铁林",

    "sex":"男",

    "email":"zhangtieli@123.com",

    "url":"./img/2.jpg"

  },

  {

    "name":"邓婕",

    "sex":"女",

    "email":"zhenjie@123.com",

    "url":"./img/3.jpg"

  },

  {

    "name":"张国立",

    "sex":"男",

    "email":"zhangguoli@123.com",

    "url":"./img/4.jpg"

  },

  {

    "name":"张铁林",

    "sex":"男",

    "email":"zhangtieli@123.com",

    "url":"./img/5.jpg"

  },

  {

    "name":"邓婕",

    "sex":"女",

    "email":"zhenjie@123.com",

    "url":"./img/6.jpg"

  }

]
'''
    print([string.split('\n')])
    # print(arr[2:])
