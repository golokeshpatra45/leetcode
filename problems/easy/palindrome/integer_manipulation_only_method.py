class Solution(object):
    def isPalindrome(self, x):

        def reverseInt(n):
            c=len(str(n))-1
            s=0
            while n>0:
                
                r=n%10
                s+=r*pow(10,c)
                n=n//10
                c-=1
            
            return s
            
        if (x<0):
            return False
        elif (x==reverseInt(x)):
            return True
        else:
            return False
