from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self, arr: list) -> None:
        self.size = len(arr)
        self.arr = arr
        self.build()

    @staticmethod
    def getLeftChild(i):
        return 2 * i + 1

    @staticmethod
    def getRightChild(i):
        return 2 * i + 2

    @staticmethod
    def getParent(i):
        return (i - 1) // 2

    @abstractmethod
    def heapify(self, array, i):
        ...

    def build(self):
        end = self.size - 1
        for i in range(end, -1, -1):
            self.heapify(self.arr, i)

    def pop(self):
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.build()

    def push(self, value):
        self.arr.insert(self.size, value)
        self.size += 1
        self.build()

    def __repr__(self):
        return f'{self.arr[:self.size]}'



class MaxHeap(Heap):
    def heapify(self, array, i):
        largest = i
        left = self.getLeftChild(i)
        right = self.getRightChild(i)
        if left < self.size and array[left] > array[i]:
            largest = left
        if right < self.size and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[largest], array[i] = array[i], array[largest]
            self.heapify(array, largest)


class MinHeap(Heap):
    def heapify(self, array, i):
        smallest = i
        left = self.getLeftChild(i)
        right = self.getRightChild(i)
        if left < self.size and array[left] < array[i]:
            smallest = left
        if right < self.size and array[right] < array[smallest]:
            smallest = right
        if smallest != i:
            array[smallest], array[i] = array[i], array[smallest]
            self.heapify(array, smallest)


new_max_heap = MaxHeap([1, 10, 21, 34, 56, 14, 31, 65])
print(new_max_heap)
new_min_heap = MinHeap([1, 10, 21, 34, 56, 14, 31, 65])
print(new_min_heap)
new_max_heap.pop()
new_min_heap.pop()
print(new_max_heap)
print(new_min_heap)
new_max_heap.push(78)
new_min_heap.push(0)
print(new_max_heap)
print(new_min_heap)






