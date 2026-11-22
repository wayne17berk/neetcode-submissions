
class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        maxamount=0
        while l<r:
            amount=min(h[l],h[r])*abs(r-l)
            maxamount=max(maxamount, amount)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return maxamount