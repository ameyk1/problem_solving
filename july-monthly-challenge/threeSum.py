# solution was understood from
# https://youtu.be/-AMHUdZc9ss
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        three_sum_list = set() # to collect unique elements
        for i in range(0, n-2):
            start = i+1
            end = n-1
            while (start < end):
                if nums[i]+nums[start]+nums[end] == 0:
                    three_sum_list.add((nums[i], nums[start], nums[end]))
                    start+=1
                    end-=1
                elif nums[i]+nums[start]+nums[end] < 0:
                    start+=1
                else:
                    end-=1

        return list(three_sum_list)


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    threesum_list = sol.threeSum(nums)
    print(threesum_list)

if __name__ == '__main__':
    main()