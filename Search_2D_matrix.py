class Solution(object):
    def searchMatrix(self, matrix, target):
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        def find_row(matrix, target, start, end):
            if start == end:
                return start
            elif end - start == 1:
                if target >= matrix[end][0]:
                    return end
                else:
                    return start
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                return find_row(matrix, target, start, end=mid - 1)
            else:
                return find_row(matrix, target, start=mid, end=end)

        def binary_search(array, target, start, end):
            if end - start == 1:
                if array[start] == target:
                    return start
                elif array[end] == target:
                    return end
                return
            elif start == end:
                if array[start] == target:
                    return start
                else:
                    return

            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            if target < array[mid]:
                return binary_search(array, target, start, end=mid - 1)
            else:
                return binary_search(array, target, start=mid + 1, end=end)

        end_index = len(matrix) - 1
        row = find_row(matrix, target, start=0, end=end_index)
        end_index = len(matrix[0]) - 1
        nums = matrix[row]
        col = binary_search(nums, target, start=0, end=end_index)

        return col is not None


if __name__ == '__main__':
    mat = [[1],[3]]
    sol = Solution()
    print(sol.searchMatrix(mat, 3))
