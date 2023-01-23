class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def rev(s):
            s=list(s)
            s.sort()
            s=''.join(s)
            return s

        res=[]
        index=[]
        for i in range(len(strs)):
            temp_arr=[]
            temp=rev(strs[i])
            if i in index:
                continue
            temp_arr.append(strs[i])
            index.append(i)
            for j in range(i+1,len(strs)):
                if temp==rev(strs[j]) and i!=j and j not in index:
                    temp_arr.append(strs[j])
                    index.append(j)
                j+=1
            res.append(temp_arr)
        return(res)
