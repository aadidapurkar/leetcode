from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColour = image[sr][sc]
        newColour = color
        newImg = None
        image[sr][sc] = newColour

        neighbours = [(sr-1,sc), (sr+1,sc), (sr, sc+1), (sr, sc-1) ]

        for neighbour in neighbours:
            newImg = self.auxFloodFill(image, neighbour[0], neighbour[1], ogColour, newColour)
        return newImg

    def auxFloodFill(self, image, sr,sc, ogColour, newColour):
        if sr < len(image) and sc < len(image[0]):
            if image[sr][sc]== ogColour:
                image[sr][sc] = newColour
                neighbours = [(sr-1,sc), (sr+1,sc), (sr, sc+1), (sr, sc-1) ]
                for neighbour in neighbours:
                    self.auxFloodFill(image, neighbour[0], neighbour[1], ogColour, newColour)
        return image        
        
        
sol = Solution()
res = sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(res)