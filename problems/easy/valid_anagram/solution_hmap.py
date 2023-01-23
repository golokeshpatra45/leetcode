class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        original_hmap={}
        new_hmap={}

        for i in range(len(s)):
            if s[i] in original_hmap:
                original_hmap[s[i]]=original_hmap[s[i]]+1
            else:
                original_hmap[s[i]]=1
            if t[i] in new_hmap:
                new_hmap[t[i]]=new_hmap[t[i]]+1
            else:
                new_hmap[t[i]]=1

        if original_hmap == new_hmap:
            return True
        else:
            return False
