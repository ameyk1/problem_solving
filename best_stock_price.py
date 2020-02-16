import numpy as np

'''
Complexity O(N2)
class Solution:
    def maxProfit(self, prices):
        max_profit=0
        for i in range (0,len(prices)):
            profit = np.max(prices[i:len(prices)]) - prices[i]
            if profit > max_profit:
                max_profit = profit

        return max_profit
'''
# Complexity O(n)
class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = 10e9, 0
        for ppd in prices:
            min_price = min(ppd,min_price)
            max_profit = max(max_profit, ppd-min_price)
        return max_profit

def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))

if __name__ == "__main__":
    main()