class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a-c>=0:
        #             dp[a]=min(dp[a-c]+1, dp[a])
        # return dp[amount] if dp[amount]<amount+1 else -1


        for c in coins:
            for i in range(c, amount+1):
                dp[i]=min(dp[i-c]+1, dp[i])
        return dp[amount] if dp[amount]<amount+1 else -1