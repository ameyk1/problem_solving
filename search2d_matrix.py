class Solution:
    def searchMatrix(self, matrix , target):
        if not matrix or matrix == [[]] or target < matrix[0][0] or target > matrix[-1][-1] :
            return False
        row, col = len(matrix), len(matrix[0])
        row_search = 0
        for i in range(row):
            if matrix[i][0] > target:
                row_search=i
                break
        for i in range (col):
            if matrix[row_search-1][i] == target or matrix[-1][i] == target:
                return True
        return False
def main():
    sol = Solution()
    matrix = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 13
    print(sol.searchMatrix(matrix, target))

if __name__ =="__main__":
    main()