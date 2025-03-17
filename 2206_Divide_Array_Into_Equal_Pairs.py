class Solution(object):
    def divideArray(self, nums):
    # solution with hashmap
        hash_map = set()

        for n in nums:
            if n in hash_map:
                hash_map.remove(n)
            else:
                hash_map.add(n)
        
        return len(hash_map) == 0
        

    # intial solution
        # count = {}
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        
        # for value in count.values():
        #     if value % 2 != 0:
        #         return False
        
        # return True
                
        