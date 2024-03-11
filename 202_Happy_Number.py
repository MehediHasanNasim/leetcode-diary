class Solution(object):
    def isHappy(self, n):
        
        value = set()
        while n not in value:
            value.add(n)
            n = self.sumofSquare(n)
            if n == 1:
                return True
        return False

    def sumofSquare(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


        