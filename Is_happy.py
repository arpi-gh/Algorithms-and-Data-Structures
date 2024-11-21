class Solution(object):
    def isHappy(self, n):
        nums = []
        number = n
        res = 0
        while True:
            while number > 0:
                res += (number % 10) ** 2
                number //= 10
            if res == 1:
                return True
            elif res in nums:
                return False
            else:
                nums.append(res)
                number = res
                res = 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(19))