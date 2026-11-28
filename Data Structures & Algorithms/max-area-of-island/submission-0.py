class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # directions=[[-1,0],[1,0],[0,1],[0,-1]]
        # rows,cols=len(grid), len(grid[0])
        # area=0
        # curr=0
        # def dfs(r,c):
        #     if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0"):
        #         return
        #     area=max(area, curr)
        #     grid[r][c]="0" 
        #     for dr,cr in directions:
        #         dfs(r+dr, c+dc)
        # for r,c in range(rows, cols):
        #     if grid[r][c]=="1":
        #         curr+=1
        #         dfs(r,c)
        # return area



        directions=[[1,0],[-1,0], [0,1],[0,-1]]
        rows,cols=len(grid), len(grid[0])
        max_area=0
        def dfs(r,c):
            if r<0 or c<0 or c>=cols or r>=rows or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            for dr,dc in directions:
                area+=dfs(r+dr, c+dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    max_area=max(max_area, dfs(r,c))

        return max_area                






    