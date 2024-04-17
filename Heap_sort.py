def max_heapify(array, index, size=None):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < size and array[left] > array[index]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        max_heapify(array, largest, size=size)


def build(array, size):
    for i in range((size//2)-1, -1, -1):
        max_heapify(array, i, size)


def heap_sort(array):
    size = len(array)
    build(array, size)
    while size > 0:
        last = size - 1
        array[0], array[last] = array[last], array[0]
        size -= 1
        max_heapify(array, index=0, size=size)


ls = [2, 8, 5, 3, 9, 1, 4]
ls1 = [1]
ls2 = []
ls3 = [1, 1, 1, 1, 1]
ls4 = [8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(ls)
heap_sort(ls1)
heap_sort(ls2)
heap_sort(ls3)
heap_sort(ls4)
print(ls)
print(ls1)
print(ls2)
print(ls3)
print(ls4)



