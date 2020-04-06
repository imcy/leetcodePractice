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

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 8]))