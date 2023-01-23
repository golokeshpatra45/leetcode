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
        hmap={}
        for i in range(len(strs)):
            if rev(strs[i]) not in hmap:
                hmap[rev(strs[i])]=[strs[i]]
            else:
                hmap[rev(strs[i])]+=[strs[i]]
        return(list(hmap.values()))
