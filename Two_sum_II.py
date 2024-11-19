class Solution(object):
    def twoSum(self, numbers, target):
        archive = {}
        for i in range(len(numbers)):
            if numbers[i] in archive:
                return archive[numbers[i]]+1, i+1
            else:
                archive[target-numbers[i]] = i