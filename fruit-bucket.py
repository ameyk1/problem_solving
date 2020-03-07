import math
class Solution():
    def __init__(self, fruit_types, basket_arr, basket_cost_arr):
        self.fruit_types = fruit_types
        self.basket_arr = basket_arr
        self.basket_cost_arr = basket_cost_arr

    def fruit_bucket(self):
        cost = [0]*self.fruit_types
        bucket_counter =0
        for i in self.basket_arr:
            cost[i-1]+=self.basket_cost_arr[bucket_counter]
            bucket_counter+=1
        return self.find_minimum(cost)

    def find_minimum(self,cost_array):
        cost_array_min = math.inf
        for i in range (0,len(cost_array)):
            if cost_array[i]<cost_array_min and cost_array[i] !=0:
                cost_min_i = i
        return cost_min_i

def main():
    try:
        TestCase = int(input())
        for i in range(0, TestCase):
            num_baskets = int(input())
            fruit_types = int(input())
            basket_arr = list(map(int, input().split(" ")) )#[int(input()) for i in range(num_baskets)] #[1, 2, 3, 3, 2, 2]
            basket_cost_arr = list(map(int, input().split(" "))) #[int(input()) for i in range(num_baskets)] #[7, 3, 9, 1, 1, 1]
            sol = Solution(fruit_types, basket_arr, basket_cost_arr)
            cost_per_fruit_type = sol.fruit_bucket()
            print(cost_per_fruit_type)
    except:
        pass
if __name__ == '__main__':
    main()

