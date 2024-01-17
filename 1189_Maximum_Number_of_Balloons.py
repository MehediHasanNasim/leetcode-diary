class Solution(object):
    def maxNumberOfBalloons(self, text):
        countText = Counter(text)
        balloon = Counter('balloon')
        
        res = len(text)
        for c in balloon:
            res = min(countText[c] // balloon[c])
            
        return res 