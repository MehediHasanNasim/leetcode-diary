class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        numSet1, numSet2 = set(nums1), set(nums2)
        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2:
                res1.add(n)
        
        for n in nums2:
            if n not in nums1:
                res2.add(n)
        
        return (list(res1), list(res2))