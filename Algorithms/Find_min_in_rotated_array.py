class Solution(object):
    def findMin(self, nums, start=0, end=None):
        if end is None:
            end = len(nums) - 1
        mid = (start + end) // 2
        if start == end or nums[start] < nums[mid] < nums[end]:
            return nums[start]
        elif mid == start:
            return min(nums[start], nums[end])
        elif nums[mid] < nums[start] and nums[mid] < nums[end]:
            return self.findMin(nums, start, end=mid)
        elif nums[mid] > nums[start] and nums[mid] > nums[end]:
            return self.findMin(nums, start=mid+1, end=end)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]
    sol = Solution()
    print(sol.findMin(arr))
