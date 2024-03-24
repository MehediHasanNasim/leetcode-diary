class Solution(object):
    def addToArrayForm(self, num, k):
       
        # Noob level of solve :) 
        output_string = ''.join(map(str, num))
        output_integer = int(output_string)

        val = output_integer + k

        res = str(val)
        output_res = [int(char) for char in res]

        return output_res



        # Bit manipulation
        num.reverse()
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            
            carry = num[i] // 10
            num[i] = num[i] % 10

            k = k // 10
            k += carry
            i += 1
        num.reverse()

        return num

