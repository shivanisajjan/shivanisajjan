
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/


# can be done still better
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        civilian_count = {}
        prev = mat[0].count(1)
        for i in range(len(mat)):
            civilian_count[i] = mat[i].count(1)
        civilian_count = dict(sorted(civilian_count.items(), key=lambda kv: (kv[1], kv[0])))
        result = []
        for keys in civilian_count.keys():
            if k == 0:
                break
            result.append(keys)
            k -= 1
        return result



# https://leetcode.com/problems/flipping-an-image/

# My Solution

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image

# https: // leetcode.com / problems / flood - fill /
    class Solution:
        def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            R, C = len(image), len(image[0])
            actualColor = image[sr][sc]
            if actualColor == newColor:
                return image

            def dfs(r, c):
                if image[r][c] == actualColor:
                    image[r][c] = newColor
                    if r > 0: dfs(r - 1, c)
                    if r < R - 1: dfs(r + 1, c)
                    if c > 0: dfs(r, c - 1)
                    if c < C - 1: dfs(r, c + 1)

            dfs(sr, sc)
            return image