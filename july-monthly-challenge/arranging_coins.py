# July Monthly Challenge
class Solution:
    def arrangeCoins(self, n):
        num_coins_req = 0
        count_steps =0
        k = 1
        while (n - num_coins_req) >= k:
            num_coins_req +=k
            k+=1
            count_steps+=1
        return count_steps

def main():
    sol = Solution()
    steps = sol.arrangeCoins(n=8)
    print(steps)

if __name__ == '__main__':
    main()


