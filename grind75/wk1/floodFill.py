from tabulate import tabulate
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, og = None) -> List[List[int]]:
        if og is None:
            og = image[sr][sc]

        if sc < 0 or sr < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1:
            return
        
        if image[sr][sc] == color:
            return
        
        neighbours = [(sr-1,sc),(sr+1,sc),(sr,sc-1),(sr,sc+1)]
        for n in neighbours:
            if image[n[0]][n[1]] == og:
                image[n[0]][n[1]] = color
                self.floodFill(image, n[0], n[1], color, og)

        
    
sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))