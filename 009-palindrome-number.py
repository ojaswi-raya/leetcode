class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        r=0
        c=x
        while x!=0:
            r=r*10+x%10
            x=x//10
        return r==c
        