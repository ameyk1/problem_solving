class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dyn_mem = [1]* n
        dyn_mem[0] = nums[0]
        dyn_mem[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dyn_mem[i] = max(nums[i]+dyn_mem[i-2], dyn_mem[i-1]) #Bottom up approach
        return dyn_mem[n-1]
def main():
    nums =  [2,1,1,2]
    sol = Solution()
    print(sol.rob(nums))

if __name__ == '__main__':
    main()