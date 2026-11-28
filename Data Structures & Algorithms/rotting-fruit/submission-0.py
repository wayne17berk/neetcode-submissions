class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        fresh=0
        time=0
        rows,cols=len(grid), len(grid[0])
        directions=[[0,-1],[-1,0],[0,1],[1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    nextrow,nextcol=r+dr, c+dc
                    if nextrow>=0 and nextcol>=0 and nextrow<rows and nextcol<cols and grid[nextrow][nextcol]==1:
                        grid[nextrow][nextcol]=2
                        q.append([nextrow,nextcol])
                        fresh-=1
            time+=1
        return time if fresh==0 else -1             