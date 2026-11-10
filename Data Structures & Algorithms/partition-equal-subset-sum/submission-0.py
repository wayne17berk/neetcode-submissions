class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False
        S = sum(nums)
        if S % 2: return False
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for s in range(target, x-1, -1):  
                if dp[s-x]:           
                    dp[s] = True
        return dp[target]   
        