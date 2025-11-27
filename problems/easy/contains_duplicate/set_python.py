class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)
        return False

        
