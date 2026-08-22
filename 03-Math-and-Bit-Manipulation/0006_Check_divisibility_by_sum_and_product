class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum =0
        product=1

        temp=n
        while temp>0:
            digit=temp%10
            digit_sum=digit_sum+digit
            product=product*digit
            temp=temp//10

        total=digit_sum+product
    
        return n%total==0
        