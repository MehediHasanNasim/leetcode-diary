class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        
        res = 0
        seen = defaultdict(int)

        for i in range(len(dominoes)):
            curr = (min(dominoes[i]), max(dominoes[i]))
            res += seen[curr]
            seen[curr] += 1 
        return res


