import collections
class Solution(object):
    def updateMatrix(self,matrix):
        def checkNeighbours(i,j):
            for er, ec in (1,0), (-1,0), (0,1), (0,-1):
                mi,mj = i+er, j+ec
                if 0<=mi<row and 0<=mj<column:
                    yield mi, mj

        row, column = len(matrix), len(matrix[0])
        q = collections.deque([])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = float('Inf')

        while q:
            i,j = q.popleft()

            for mi, mj in checkNeighbours(i,j):
                if matrix[mi][mj] > matrix[i][j]+1:
                    matrix[mi][mj] = matrix[i][j] + 1
                    q.append((mi,mj))

        return matrix


def main():
    sol = Solution()
    a = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    a_out =sol.updateMatrix(a)
    print(a_out)

if __name__ =="__main__":
    main()