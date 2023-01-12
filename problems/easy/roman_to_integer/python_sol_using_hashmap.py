class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        
        for i in range(len(s)):
            if i<len(s)-1 and symbols[s[i]] < symbols[s[i+1]]:
                temp=-symbols[s[i]]
                sum=sum+temp
            else:
                sum=sum+symbols[s[i]]
        return(sum)
