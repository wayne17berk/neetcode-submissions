class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        res=nums[0]
        for num in nums:
            cur=max(cur,0)+num
            res=max(res, cur)
        return res
        