class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        original = list(s)
        new = list(t)
        original.sort()
        new.sort()
        if original==new:
            return True
        else:
            return False
