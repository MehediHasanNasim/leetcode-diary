class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # two pointer // time o(n), space o(1)
        l ,r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l , r = l + 1, r - 1
            
        # Stack // time o(n), space o(n)
        stack = []
        for c in s:
            stack.append(c)
        i = 0 
        while stack:
            s[i] = stack.pop()
            i += 1