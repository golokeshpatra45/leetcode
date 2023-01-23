import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.sub('[^A-Za-z0-9]+','',s).lower().replace(" ","")[::-1] == re.sub('[^A-Za-z0-9]+','',s).lower().replace(" ","")
