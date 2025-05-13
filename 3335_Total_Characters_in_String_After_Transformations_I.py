class Solution(object):
    def lengthAfterTransformations(self, s, t):
        MOD = 10**9 + 7

        count = [0] * 26 
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(25): 
                new_count[i + 1] = (new_count[i + 1] + count[i]) % MOD
            new_count[0] = (new_count[0] + count[25]) % MOD
            new_count[1] = (new_count[1] + count[25]) % MOD
            count = new_count

        return sum(count) % MOD


