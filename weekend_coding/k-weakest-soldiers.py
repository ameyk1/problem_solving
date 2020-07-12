class Solution:
    def kWeakestRows(self, mat, k):
        out = []
        for rows in range (0,len(mat)):
            out.append([mat[rows].count(1), rows])
        out.sort()
        out_k = list(out[rows][1] for rows in range(k))
        return out_k

def main():
    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    k = 3
    sol = Solution()
    print(sol.kWeakestRows(mat,k))

if __name__ == '__main__':
    main()