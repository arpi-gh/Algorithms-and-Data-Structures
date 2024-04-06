class Solution:
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums)-1):
    #         if nums[i] ^ nums[i+1] == 0:
    #             return True
    #     return False
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers ={}
        for num in nums:
            if num in numbers:
                return True
            else:
                numbers[num] = 1
        return False