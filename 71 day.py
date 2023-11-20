class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]=1
        ans=pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            ans+=count[pre-k]
            count[pre]+=1
        return ans
        
