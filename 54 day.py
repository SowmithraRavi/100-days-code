#gfs
class Solution:
    def missingNumber(self,array,n):
        sum_N = n * (n + 1) // 2
        sum_A = sum(array)
        missing_element = sum_N - sum_A
        return missing_element

#leetcode
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1]+1
