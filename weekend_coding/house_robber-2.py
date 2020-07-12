class Solution:
    def rob(self, nums):
        n = len(nums)
        if n < 3:
            if n == 0 : return 0
            elif n == 1 : return nums[0]
            elif n ==2 : return max(nums[0], nums[1])
        return max (nums[0] + self.prev_robber(nums[2:-1]), self.prev_robber(nums[1:]))

    def prev_robber(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dyn_mem = [1] * n
        dyn_mem[0] = nums[0]
        dyn_mem[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dyn_mem[i] = max(nums[i]+dyn_mem[i-2], dyn_mem[i-1]) #Bottom up approach
        print(dyn_mem)
        return dyn_mem[-1]
def main():
    nums = [1,2,3,1]
    sol = Solution()
    print(sol.rob(nums))

if __name__ == '__main__':
    main()