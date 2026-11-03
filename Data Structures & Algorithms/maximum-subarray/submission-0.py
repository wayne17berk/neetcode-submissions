class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, res=0, nums[0]
        for num in nums:
            cur= max(cur,0)+num
            res=max(cur, res)
        return res
        