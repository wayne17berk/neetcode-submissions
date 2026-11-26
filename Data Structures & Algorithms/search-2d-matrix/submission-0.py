class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix), len(matrix[0])
        top,bot=0,rows-1
        while top<=bot:
            therow=(top+bot)//2
            if target<matrix[therow][0]:
                bot=therow-1
            elif target>matrix[therow][-1]:
                top=therow+1
            else:
                break

        l,r=0,cols-1
        while l<=r:
            m=(l+r)//2
            if target<matrix[therow][m]:
                r=m-1
            elif target>matrix[therow][m]:
                l=m+1
            else:
                return True
        return False