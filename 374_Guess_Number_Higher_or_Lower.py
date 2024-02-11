
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
            
