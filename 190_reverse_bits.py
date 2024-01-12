class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):           # take 32 place as it was 32 page
            bit = (n >> i) & 1        # extracting i and original value of n is shifted in i with multiplying 1
            res |= (bit << (31 - i))  # as res = 0 in given value, reverse the value by (31-i) and shift it in bit. add with res
        return res
    
 