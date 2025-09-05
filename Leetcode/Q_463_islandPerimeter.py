class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ''' 
        **TODO: Fix this sphaghetti code later

        General Approach:  

        NOTE: 4 represents the total permieter of land cells
        (entirely surrounded by water). 

        - Traverse through the matrix using something 
        like DFS, going to neighboring land cells each time. 
        If the neighboring cell is a "1", subtract 4 by 1. 
        ''' 

        start = grid[0][0]

        self.dfs_help(grid, grid[0], grid[0], )


    def dfs_help(self, grid, row, col, currcell_val, perimeter): 

        if row >= len(grid) or row < 0 or col >= len(grid[0]):
            return 


        if grid[row][col] == 1:
            currcell_val = 4 
            currcell_val -= 1
            


        # check adjacent cells 
        # up 
        self.dfs_help(grid, row - 1, col, currcell_val, nextcell_val)

        # left
        self.dfs_help(grid, row, col - 1, currcell_val, nextcell_val)

        # right 
        self.dfs_help(grid, row, col + 1, currcell_val, nextcell_val)

        # down 
        self.dfs_help(grid, row + 1, col, currcell_val, nextcell_val)

