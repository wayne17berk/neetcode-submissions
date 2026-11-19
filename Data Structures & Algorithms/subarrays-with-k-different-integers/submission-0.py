class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            cnt=defaultdict(int)
            l=res=0
            for r,x in enumerate(nums):
                cnt[nums[r]]+=1
                while len(cnt)>k:
                    cnt[nums[l]]-=1
                    if cnt[nums[l]]==0:
                        del cnt[nums[l]]
                    l+=1
                res+=r-l+1
            return res
        return at_most(k)-at_most(k-1)