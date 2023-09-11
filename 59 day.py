class Solution(object):
    def twoSum(self, nums, target):
        n=[]
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    n.append(i)
                    n.append(j)
        return n
