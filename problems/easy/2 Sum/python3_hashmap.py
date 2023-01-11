class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        c=0
        for i in range(len(nums)):
            hash[nums[i]]=c
            c+=1
        
        for i in range(len(nums)):
            if target-nums[i] in hash and i != hash[target-nums[i]]:
                return([i,hash[target-nums[i]]])
