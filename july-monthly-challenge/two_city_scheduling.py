# June monthly challenge
# https://youtu.be/vtNoP43hGJA
from heapq import heappop, heappush, heapify

class Solution:
    # O(nlogn) solution
    def twoCitySchedCost_nlogn(self, cost_list):
        schedule_cost = 0
        sorted_diff = sorted(cost_list, key=lambda x: (x[0]-x[1]))
        n = len(sorted_diff)//2
        for i in range(n):
            schedule_cost += sorted_diff[i][0]

        for i in range(n,len(sorted_diff)):
            schedule_cost += sorted_diff[i][1]

        return schedule_cost

    def twoCitySchedCost(self, cost_list):
        heap = []
        heapify(heap)
        schedule_cost = 0
        n = len(cost_list)//2
        for cost_elem in cost_list:
            heappush(heap, [cost_elem[0]-cost_elem[1], cost_elem[0], cost_elem[1]])
        for i in range(n):
            a = heappop(heap)
            schedule_cost += a[1]
        for i in range(n, len(cost_list)):
            a = heappop(heap)
            schedule_cost += a[2]
        return schedule_cost

def main():
    cost_list = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    sol = Solution()
    schedule_cost = sol.twoCitySchedCost(cost_list)
    schedule_cost_nlogn = sol.twoCitySchedCost_nlogn(cost_list)
    print(schedule_cost)
    print(schedule_cost_nlogn)

if __name__ == '__main__':
    main()