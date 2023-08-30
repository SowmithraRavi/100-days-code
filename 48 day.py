class Solution(object):
    def removeDuplicates(self, nums):
        u = 1
        for i in range(1,len(nums)):
            if(nums[i-1]!=nums[i]):
                nums[u] = nums[i]
                u+=1
        return u
