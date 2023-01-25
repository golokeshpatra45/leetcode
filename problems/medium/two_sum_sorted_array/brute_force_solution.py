class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0
        res=[]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if target-numbers[i]==numbers[j]:
                    res.append(i+1)
                    res.append(j+1)
                    return (res)
