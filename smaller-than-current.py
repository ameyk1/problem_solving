import numpy as np
class Solution_wSort():
    def smallerNumbersThanCurrent(self, nums):
        output = []
        nums_sorted = tuple(np.sort(nums))
        for i in nums:
            output.append(nums_sorted.index(i))
        return output

class Solution():
    def smallerNumbersThanCurrent(self, nums):
        nums_bucket = [0]*101
        for num in nums:
            nums_bucket[num]+=1
        accumulate = [0]*101
        for i in range(1,101):
            accumulate[i]= accumulate[i-1]+nums_bucket[i-1]
        return [accumulate[num] for num in nums]
def main():
    nums = [8, 8, 77, 1, 2]
    print(nums)
    sol = Solution_wSort()
    print(sol.smallerNumbersThanCurrent(nums))
    sol = Solution()
    print(sol.smallerNumbersThanCurrent(nums))

if __name__ == '__main__':
    main()
