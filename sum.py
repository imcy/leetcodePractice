class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            find = target - num
            res = hash_map.get(find)
            if res is not None:
                return [i, res]
            hash_map[num] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 3], 6))
