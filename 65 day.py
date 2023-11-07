class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
           j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]   
   
