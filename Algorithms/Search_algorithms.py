class Search:
    @staticmethod
    def binary_search(array, target, start=0, end=None) -> int:
        if end is None:
            end = len(array)-1
        mid = (start + end) // 2
        if len(array) == 0:
            return -1
        if target == array[start]:
            return start
        elif target == array[end]:
            return end
        elif target == array[mid]:
            return mid
        else:
            if array[start] < target < array[mid]:
                return Search.binary_search(array, target, start=0, end=mid)
                # remember to return the function here, otherwise it returns None
            if array[mid] < target < array[end]:
                return Search.binary_search(array, target, start=mid, end=len(array)-1)


if __name__ == '__main__':
    search = Search()
    ls = [1, 2, 3, 6, 5, 7, 8, 9, 4, 10]
    ls.sort()
    print('Binary Search: ', search.binary_search(ls, 8))

