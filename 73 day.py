class Solution(object):
    def majorityElement(self, nums):
        ele = Counter(nums)
        major_ele = []
        t = len(nums) // 3
        for element, count in ele.items():
            if count > t:
                major_ele.append(element)
        
        return major_ele
        
