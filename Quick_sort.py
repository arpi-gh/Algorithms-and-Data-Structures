def quick_sort(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    if end-start == 1:
        if nums[start] > nums[end]:
            nums[start], nums[end] = nums[end], nums[start]
    if end > start:
        pivot = nums[start]
        nums[start], nums[end] = nums[end], nums[start]
        j = end-1
        for i in range(start, end+1):
            if nums[i] > pivot:
                while j > start-1:
                    if nums[j] < pivot and i != j:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    elif i == j:
                        nums[i], nums[end] = nums[end], nums[i]
                        return quick_sort(nums, start=start, end=i-1), quick_sort(nums, start=i+1, end=end)
                    j -= 1
            elif i > j:
                return quick_sort(nums, start=start, end=i-1)
    return


ls1 = [5, 3, 8, 1, 9, 2, 7, 4, 6]
ls2 = [5, 3, 1, 4, 7]
ls3 = [4]
ls4 = [1, 3, 2]
ls5 = [1, 2, 3]
ls6 = []
quick_sort(ls1)
quick_sort(ls2)
quick_sort(ls3)
quick_sort(ls4)
quick_sort(ls5)
quick_sort(ls6)
print(ls1)
print(ls2)
print(ls3)
print(ls4)
print(ls5)
print(ls6)