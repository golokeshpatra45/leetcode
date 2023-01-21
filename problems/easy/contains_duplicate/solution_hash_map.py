class Solution(object):
    def containsDuplicate(self, nums):
        h_map = {}
        for i in range(len(nums)):
            if nums[i] not in h_map:
                h_map[nums[i]]=1
            else:
                h_map[nums[i]]=h_map[nums[i]]+1
            if h_map[nums[i]] > 1:
                return True
        
        return False
