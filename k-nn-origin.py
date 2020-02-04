from heapq import heappush, heappop, heappushpop

class Solution():
    def pt2origin(self, pt):
        x, y = pt[0], pt[1]
        return x**2 + y**2
    def kClosest(self, points, K):
        k_distance = []
        for i in range (K):
            heappush(k_distance, (-self.pt2origin(points[i]), points[i])) # Using negative value due to heap
        for i in range (K, len(points)):
            heappushpop(k_distance, (-self.pt2origin(points[i]),points[i]))
        return [heappop(k_distance)[1] for _ in range(K)]

def main():
    points = [[1, 3], [-2, 2]]
    K = 1
    sol = Solution()
    print(sol.kClosest(points, K))

if __name__ == "__main__":
    main()