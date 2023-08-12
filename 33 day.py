#Armstrongnumber
class Solution:
    def armstrongNumber (self, n):
        k=int(n) 
        rem=0 
        sum=0
        while(n>0):
            rem=n%10 
            sum=sum+(rem**3) 
            n=int(n/10) 
            
        if(k==sum):
            return 'Yes' 
        else:
            return 'No'
 
#Palindrome
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
           return False 
        k=x 
        reverse=0 
        rem=0
        while(x!=0):
            rem=x%10
            reverse=reverse*10 + rem
            x=x//10
        return reverse==k
           
