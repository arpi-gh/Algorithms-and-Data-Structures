class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        high = 10 ** (int(len(str(x))) - 1)
        low = 10
        while high != 0:
            first = x // high
            last = x % 10
            if first != last:
                return False
            x = (x - (x // high) * high) // 10
            high //= 100
        return True
