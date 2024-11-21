class Solution(object):
    # Time limit exceeded
    # def rotate(self, nums, k):
    #     k %= len(nums)
    #     if k == 0:
    #         return
    #     right = len(nums) - 1
    #     for i in range(len(nums) - k):
    #         left = right - k
    #         while left < right:
    #             nums[left], nums[left + 1] = nums[left + 1], nums[left]
    #             left += 1
    #         right -= 1
    #     return

    def rotate(self, nums, k):
        k %= len(nums)
        if k == 0:
            return
        nums.reverse()
        left = 0
        right = k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left = k
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



