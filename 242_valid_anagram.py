class Solution(object):
    def isAnagram(self, s, t):
        ''' solution 3 '''
        return sorted(s) == sorted(t)

        """ solution 2 """
        return Counter(s) == Counter(t)

        """ solution 1 """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        """ Solution 0 """
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in s:
            countS[i] = countS.get(i, 0) + 1
        for i in t:
            countT[i] = countT.get(i, 0) + 1
        
        return countS == countT