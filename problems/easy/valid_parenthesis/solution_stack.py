class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets={')':'(',
                    '}':'{',
                    ']':'[',
                    }
        stack=[]
        for i in s:
            if i not in brackets:
                stack.append(i)
            else:
                if not stack:
                    return(False)
                if brackets[i]!=stack.pop():
                    return(False)
        return not stack
