
class Solution(object):
    def guessNumber(self, n):

        low = 1
        high = n
        
        while True:
            mid = low + (high - low) // 2
            myGuess = guess(mid)
            if myGuess == 1:
                low = mid + 1
            elif myGuess == -1:
                high = mid - 1
            else:
                return mid
            
        # mine trial
        l, r = 1, n
        while True:
            mid  = (l + r) // 2
            res = guess(mid)
            if res > 0:
                l = mid + 1
            elif res < 0:
                r = mid - 1
            else:
                return mid
