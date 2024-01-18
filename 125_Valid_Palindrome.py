class Solution(object):
    def isPalindrome(self, s):
        # using built-in module
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]