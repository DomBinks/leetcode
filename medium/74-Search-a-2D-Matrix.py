class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for row in matrix:
            lst.extend(row)

        return target in lst
