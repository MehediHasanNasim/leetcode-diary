from collections import defaultdict # Not Mandatory

class Solution(object):
    def countLargestGroup(self, n):
        count = defaultdict(int)
        maxsize = 0
        
        for digit in range(1, n + 1):
            digit_sum = sum(int(Sdigit) for Sdigit in str(digit))
            count[digit_sum] += 1
            maxsize = max(maxsize, count[digit_sum])

        result_count = 0
        for size in count.values():
            if size == maxsize:
                result_count += 1

        return result_count




        