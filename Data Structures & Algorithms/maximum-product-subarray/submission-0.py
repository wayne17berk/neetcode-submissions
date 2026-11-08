class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        mx=[0]*n
        mn=[0]*n
        res=mx[0]=mn[0]=nums[0]

        for n in range(1, n):
            mx[n]=max(nums[n],mx[n-1]*nums[n],mn[n-1]*nums[n])
            mn[n]=min(nums[n],mx[n-1]*nums[n],mn[n-1]*nums[n])
            res=max(res, mx[n])
        return res