#leetcode
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[a]=nums[a],nums[i]
                a+=1
        return nums

#gfg
class Solution:
	def pushZerosToEnd(self,arr, n):
	    a=0
        for i in range(n):
            if(arr[i]!=0):
                arr[a],arr[i]=arr[i],arr[a]
                a+=1
        return arr
        
