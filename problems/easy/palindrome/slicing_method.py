class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        else:
            x=str(x)
            reversed_str=x[::-1]
            if int(reversed_str)==int(x):
                return True
            else:
                False
        
