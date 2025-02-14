class Solution(object):
    def findPeakElement(self, nums, start=0, end=None):
        if end is None:
            end = len(nums) - 1
        mid = (start + end) // 2
        if start == end:
            return start
        elif start == mid:
            if nums[start] > nums[end]:
                return start
            else:
                return end

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
            left = self.findPeakElement(nums, start, end=mid - 1)
            right = self.findPeakElement(nums, start=mid, end=end)
        elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
            left = self.findPeakElement(nums, start, end=mid)
            right = self.findPeakElement(nums, start=mid + 1, end=end)
        elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            left = self.findPeakElement(nums, start, end=mid - 1)
            right = self.findPeakElement(nums, start=mid + 1, end=end)

        if nums[left] > nums[right]:
            return left
        else:
            return right


if __name__ == '__main__':
    arr = [6, 5, 4, 3, 2, 3, 2]
    sol = Solution()
    print(sol.findPeakElement(arr))
