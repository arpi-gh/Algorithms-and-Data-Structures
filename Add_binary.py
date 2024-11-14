class Solution(object):
    def addBinary(self, a, b):
        result = ''
        carry = 0
        a, b = a[::-1], b[::-1]
        length = max(len(a), len(b))
        for d in range(length):
            digitA = int(a[d] if d < len(a) else 0)
            digitB = int(b[d] if d < len(b) else 0)
            digit = (digitA ^ digitB) ^ carry
            carry = (digitA and digitB) or carry
            result += str(digit)
        result = result[::-1]
        return result


if __name__ == "__main__":
    num1 = '11001011'
    num2 = '1011010'

    sol = Solution()
    print(sol.addBinary(num1, num2))
