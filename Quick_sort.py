def quick_sort(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    if end == start:
        return
    else:
        pivot = nums[start]
        pivot_index = start
        nums[start], nums[end] = nums[end], nums[start]
        for i in range(pivot_index, end+1):    # end is not counted
            if nums[i] > pivot:
                for j in range(end-1, i-1, -1):   # check how far this goes
                    if nums[j] < pivot:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    if i == j:
                        pivot_index = i
                        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
                        quick_sort(nums, start=start, end=pivot_index-1)
                        quick_sort(nums, start=pivot_index+1, end=end)


ls1 = [5, 3, 8, 1, 9, 2, 7, 4, 6]
ls2 = [5, 3, 1, 4, 7]
quick_sort(ls1)
print(ls1)