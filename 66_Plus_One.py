class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        while n>0:
            if digits[n-1]==9:
                if (n-1)== 0:
                    digits[n-1]=0
                    temp = [1]+ digits
                    return temp
                else:
                    digits[n-1] = 0
                    n = n-1
            else: 
                digits[n-1] += 1
                return digits
        return digits