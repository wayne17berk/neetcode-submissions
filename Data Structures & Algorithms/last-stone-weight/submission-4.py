class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i]=(-stones[i])
        heapq.heapify(stones)
        while len(stones)>0:
            if len(stones)==1:
                break    
            stone1=heapq.heappop(stones)
            stone2=heapq.heappop(stones)
            residual=abs(stone1-stone2)
            if residual>0:
                heapq.heappush(stones, -(residual))
        return abs(stones[0]) if len(stones)==1 else 0      