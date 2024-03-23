class Solution(object):
    def addToArrayForm(self, num, k):
       
        # Noob level of solve :) 
        output_string = ''.join(map(str, num))
        output_integer = int(output_string)

        val = output_integer + k

        res = str(val)
        output_res = [int(char) for char in res]

        return output_res


