class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  #  maximum consecutive 1s 
        current_count = 0  #  current consecutive 1s streak.
        for i in nums:
            if i == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        max_count = max(max_count, current_count)
        return max_count
