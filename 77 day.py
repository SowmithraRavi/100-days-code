class Solution(object):
    def beautifulSubarrays(self, nums):
        pre = [0]
        for i in nums:
            pre.append(pre[-1] ^ i)
        
        prefix_counter = Counter(pre)

        cnt = 0
        for i, c in prefix_counter.items():
            if c > 1:
                cnt += (c - 1) * c // 2
        return cnt
