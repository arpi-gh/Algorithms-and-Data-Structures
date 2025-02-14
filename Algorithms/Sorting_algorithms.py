import time

class Sort:
    @staticmethod
    def bubble_sort(array):
        for j in range(len(array)-1):  # n-1 times
            for i in range(len(array)-1):  # n-1 times
                if array[i] > array[i+1]:  # n-1 times
                    array[i], array[i+1] = array[i+1], array[i]  # n-1 times in worst case scenario
        return array
    # Time Complexity
    # (n-1)(n-1) + n-1 + n-1 = n^2 - 2n + 1 + 2n - 2 = n^2 - 1 ???

    @staticmethod
    def optimized_bubble(array):
        for i in range(len(array), -1, -1):
            swapped = False
            for j in range(i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            if not swapped:
                break
        return array

    @staticmethod
    def selection_sort(array):
        for i in range(0, len(array)-1):  # n-1 times
            min_index = i  # n-1 times
            for j in range(i+1, len(array)):  # n-1 times
                if array[j] < array[min_index]:  # n-1 times
                    min_index = j   # Remember the index of the new minimum    # n-1 - worst case
            array[i], array[min_index] = array[min_index], array[i]   # swap the places if not the same  # n-1 times
        return array
    # Time Complexity
    # (n-1)(n-1) + n-1 + n-1 + n-1 = n^2 - 2n + 1 + 3n - 3 = n^2 + n - 2 ???

    @staticmethod
    def insertion_sort(array):
        for i in range(1, len(array)):
            tmp = array[i]
            j = i-1
            while j >= 0:
                if array[j] > tmp:
                    array[i] = array[j]
                    array[j] = tmp
                i = j
                j -= 1
        return array

    @staticmethod
    def insertion_sort_optimized(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while j >=  0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return array

    @staticmethod
    def merge(left, right):
        left.extend(right)
        merged = sorted(left)
        # print(merged)
        return merged

    @staticmethod
    def merge_sort(array):
        if len(array) == 1:
            return [array[0]]   # only once
        mid = len(array) // 2   # will be called as many times as merge_sort is called
        left_subarray = Sort.merge_sort(array[:mid])  # n/2 - 1 times
        right_subarray = Sort.merge_sort(array[mid:]) # n/2 - 1 times
        # print(f'merging {left_subarray} with {right_subarray}')
        return Sort.merge(left_subarray, right_subarray)  # n-1 times, I think

    @staticmethod
    def counting_sort(nums):
        nums_range = max(nums) - min(nums)
        num_counts = (nums_range + 1) * [0]
        sorted_nums = len(nums) * [0]
        min_elem = min(nums)
        for num in nums:
            num_counts[num - min_elem] += 1
        # print(num_counts)
        # print(sorted_nums)
        num_indices = (len(num_counts) + 1) * [0]
        for i in range(len(num_counts)):
            num_indices[i + 1] = num_counts[i] + num_indices[i]
        # print(num_indices)
        index = 0
        tmp = 0
        for n in num_indices[1:]:
            for i in range(tmp, nums_range + 1):
                while index < n:
                    sorted_nums[index] = i + min_elem
                    index += 1
                tmp = i + 1
                break
        return sorted_nums

    @staticmethod
    def quick_sort(nums, start=0, end=None):
        def partition(nums, start, end):
            left = start
            right = end
            pivot_index = (start+end) // 2
            pivot = nums[pivot_index]
            nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
            while left < right:
                if nums[left] > pivot:
                    while right > left:
                        if nums[right] < pivot:
                            nums[left], nums[right] = nums[right], nums[left]
                            break
                        right -= 1
                        if left == right:
                            nums[left], nums[end] = nums[end], nums[left]
                            break
                left += 1
                if left == right:
                    nums[left], nums[end] = nums[end], nums[left]
            return left

        if end is None:
            end = len(nums) - 1
        if end-start == 1 and nums[start] > nums[end]:
            nums[start], nums[end] = nums[end], nums[end]
        if end > start:
            index = partition(nums, start, end)
            Sort().quick_sort(nums, start, index-1)
            Sort().quick_sort(nums, index+1, end)
        return nums


if __name__ == '__main__':
    sort = Sort()
    ls = [1, 4, 6, 2, -1, 8, 7, -2]
    ls1 = [4, 6, 8, 1, 2, 4, 3, -4, ]

    # start_time = time.time()
    # print('Bubble:', sort.bubble_sort(ls))
    # end_time = time.time()
    # print(end_time-start_time)
    #
    # start_time = time.time()
    # print('Optimized bubble:', sort.optimized_bubble(ls))
    # end_time = time.time()
    # print(end_time - start_time)
    #
    # start_time = time.time()
    # print('Selection:', sort.selection_sort(ls))
    # end_time = time.time()
    # print(end_time - start_time)
    #
    # start_time = time.time()
    # print('Insertion:', sort.insertion_sort(ls))
    # end_time = time.time()
    # print(end_time - start_time)
    #
    # start_time = time.time()
    # print('Insertion new:', sort.insertion_sort_optimized(ls))
    # end_time = time.time()
    # print(end_time - start_time)
    #
    # start_time = time.time()
    # print('Merge:', sort.merge_sort(ls))
    # end_time = time.time()
    # print(end_time - start_time)

    print(sort.quick_sort(ls))
