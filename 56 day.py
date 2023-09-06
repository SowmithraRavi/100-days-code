class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = nums[i] 
            c = 0
            for j in range(n):
                if nums[j] == num:
                    c += 1
            if c == 1:
                return num
        return -1
