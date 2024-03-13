class Solution(object):
    def countOdds(self, low, high):
        """time exceed"""
        # count = 0
        # for i in range(low, high + 1):
        #     if i % 2 != 0:
        #         count += 1
        # return count

        '''some error on some test case'''
        # total_val = (high - low) + 1
        # odd_num = total_val // 2
        # odd_num += (low % 2)

        # return odd_num
        

        length = (high - low) + 1
        odd_num = length // 2
        if length % 2 and low % 2:
            odd_num += 1

        return odd_num
        