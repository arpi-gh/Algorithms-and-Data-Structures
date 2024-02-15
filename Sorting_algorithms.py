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


if __name__ == '__main__':
    sort = Sort()
    ls = [1, 4, 6, 2, -1, 8, 7, -2]
    print('Bubble:', sort.bubble_sort(ls))
    print('Selection:', sort.selection_sort(ls))
    print('Insertion:', sort.insertion_sort(ls))
