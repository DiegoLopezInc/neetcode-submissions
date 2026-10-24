class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()


        def dfs(r,c):
            if (r >= ROWS or c >= COLS or
            r < 0 or c < 0 or grid[r][c] == "0" 
            or (r,c) in seen):
                return False
            
            seen.add((r,c))
            # up down left right
            res = (dfs(r-1,c) or
                dfs(r+1,c) or
                dfs(r,c-1) or
                dfs(r,c+1))
            return True
        
        def bfs(r,c):
            q = collections.deque()
            seen.add((r,c))
            q.append((r,c))
           
            while q:
                row,col = q.popleft() # iterative dfs
                directions = [[1,0],[-1,0],[0,-1],[0,1]]

                for dr, dc in directions:
                    r,c = row+dr,col+dc
                    if ((r) in range(ROWS) and
                        (c) in range(COLS) and
                        grid[r][c]=="1" and
                        (r,c) not in seen):
                        q.append((r,c))
                        seen.add((r,c))
               
            return 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r,c)
                    islands+=1
    
        return islands